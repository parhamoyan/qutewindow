#!/usr/bin/env python3
"""
Release script for CuteWindow.

This script helps automate the release process locally before pushing tags.
It performs various checks and builds the package to ensure everything is ready.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


def run_command(
    cmd: List[str], cwd: Path | None = None, check: bool = True
) -> Tuple[bool, str]:
    """Run a command and return success status and output."""
    try:
        result = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True, check=check
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr


def check_git_status() -> bool:
    """Check if git working directory is clean."""
    success, output = run_command(["git", "status", "--porcelain"])
    if not success:
        print(f"❌ Failed to check git status: {output}")
        return False

    if output.strip():
        print("❌ Git working directory is not clean:")
        print(output)
        return False

    print("✅ Git working directory is clean")
    return True


def check_version_consistency(version: str) -> bool:
    """Check if version in pyproject.toml matches the given version."""
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("❌ pyproject.toml not found")
        return False

    content = pyproject_path.read_text()
    version_pattern = r'version = "([^"]+)"'
    match = re.search(version_pattern, content)

    if not match:
        print("❌ Could not find version in pyproject.toml")
        return False

    pyproject_version = match.group(1)
    if pyproject_version != version:
        print("❌ Version mismatch:")
        print(f"   Expected: {version}")
        print(f"   Found in pyproject.toml: {pyproject_version}")
        return False

    print(f"✅ Version consistency check passed: {version}")
    return True


def check_changelog(version: str) -> bool:
    """Check if changelog has an entry for the given version."""
    changelog_path = Path("CHANGELOG.md")
    if not changelog_path.exists():
        print("❌ CHANGELOG.md not found")
        return False

    content = changelog_path.read_text()
    version_pattern = rf"## \[{re.escape(version)}\] - "

    if not re.search(version_pattern, content):
        print(f"❌ No changelog entry found for version {version}")
        return False

    print(f"✅ Changelog entry found for version {version}")
    return True


def run_quality_checks() -> bool:
    """Run code quality checks."""
    print("🔍 Running quality checks...")

    # Run black
    success, output = run_command(["poetry", "run", "black", "--check", "."])
    if not success:
        print("❌ Black formatting check failed:")
        print(output)
        return False

    # Run isort
    success, output = run_command(["poetry", "run", "isort", "--check-only", "."])
    if not success:
        print("❌ isort check failed:")
        print(output)
        return False

    # Run flake8
    success, output = run_command(["poetry", "run", "flake8", "."])
    if not success:
        print("❌ flake8 check failed:")
        print(output)
        return False

    # Run mypy
    success, output = run_command(["poetry", "run", "mypy", "."], check=False)
    if not success:
        print("⚠️  mypy check failed (but continuing):")
        print(output)

    print("✅ Quality checks passed")
    return True


def build_package() -> bool:
    """Build the package."""
    print("📦 Building package...")
    success, output = run_command(["poetry", "build"])

    if not success:
        print("❌ Package build failed:")
        print(output)
        return False

    print("✅ Package built successfully")
    return True


def test_package_installation() -> bool:
    """Test package installation."""
    print("🔧 Testing package installation...")

    # Create a temporary virtual environment
    success, output = run_command(["python", "-m", "venv", "test_env"])
    if not success:
        print("❌ Failed to create test environment:")
        print(output)
        return False

    # Install the built package
    dist_files = list(Path("dist").glob("*.whl"))
    if not dist_files:
        print("❌ No wheel file found in dist/")
        return False

    wheel_file = dist_files[0]
    success, output = run_command(
        [
            (
                "test_env/bin/pip"
                if sys.platform != "win32"
                else "test_env\\Scripts\\pip.exe"
            ),
            "install",
            str(wheel_file),
        ]
    )

    if not success:
        print("❌ Failed to install package:")
        print(output)
        return False

    # Test import
    success, output = run_command(
        [
            (
                "test_env/bin/python"
                if sys.platform != "win32"
                else "test_env\\Scripts\\python.exe"
            ),
            "-c",
            "import cutewindow; print('CuteWindow imported successfully')",
        ]
    )

    if not success:
        print("❌ Failed to import package:")
        print(output)
        return False

    print("✅ Package installation test passed")
    return True


def cleanup() -> None:
    """Clean up temporary files."""
    import shutil

    # Remove test environment
    test_env_path = Path("test_env")
    if test_env_path.exists():
        shutil.rmtree(test_env_path)

    print("🧹 Cleanup completed")


def main():
    parser = argparse.ArgumentParser(description="Prepare and validate a release")
    parser.add_argument("version", help="Version to release (e.g., 0.3.0)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running tests")
    parser.add_argument(
        "--skip-quality", action="store_true", help="Skip quality checks"
    )
    parser.add_argument(
        "--skip-build", action="store_true", help="Skip building package"
    )
    parser.add_argument(
        "--skip-install-test", action="store_true", help="Skip installation test"
    )

    args = parser.parse_args()

    print(f"🚀 Preparing release for version {args.version}")
    print("=" * 50)

    all_checks_passed = True

    # Basic checks
    all_checks_passed &= check_git_status()
    all_checks_passed &= check_version_consistency(args.version)
    all_checks_passed &= check_changelog(args.version)

    # Quality checks
    if not args.skip_quality:
        all_checks_passed &= run_quality_checks()

    # Tests
    if not args.skip_tests:
        print("⚠️  Tests are disabled in this build")

    # Build
    if not args.skip_build:
        all_checks_passed &= build_package()

    # Installation test
    if not args.skip_install_test and not args.skip_build:
        all_checks_passed &= test_package_installation()

    # Cleanup
    cleanup()

    print("=" * 50)
    if all_checks_passed:
        print("✅ All checks passed! Ready for release.")
        print("\nTo create the release:")
        print("1. Commit any changes if needed")
        print(
            f"2. Create and push tag: git tag v{args.version} && "
            f"git push origin v{args.version}"
        )
        print("3. Or trigger manual release through GitHub Actions")
        return 0
    else:
        print("❌ Some checks failed. Please fix the issues above before releasing.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
