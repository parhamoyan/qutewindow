#!/usr/bin/env python3
"""
Comprehensive test runner script for QuteWindow.

This script runs various test suites including unit tests, coverage tests,
and integration tests.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


class Colors:
    """ANSI color codes for terminal output."""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    NC = "\033[0m"  # No Color


def print_status(color: str, message: str) -> None:
    """Print colored status message."""
    print(f"{color}📋 {message}{Colors.NC}")


def run_command(command: List[str], description: str) -> Tuple[bool, str]:
    """Run a command and return success status and output."""
    print()
    print_status(Colors.BLUE, f"Running {description}...")
    print(f"Command: {' '.join(command)}")
    print("-" * 50)

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        return result.returncode == 0, result.stdout + result.stderr
    except Exception as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return False, str(e)


def check_directory() -> bool:
    """Check if we're in the project root directory."""
    if not Path("pyproject.toml").exists():
        print_status(
            Colors.RED,
            "❌ Error: Please run this script from the project root directory",
        )
        return False
    return True


def check_dependencies() -> bool:
    """Check if pytest is installed."""
    print_status(Colors.BLUE, "📦 Checking dependencies...")

    result = subprocess.run(
        ["poetry", "show", "pytest"], capture_output=True, text=True
    )

    if result.returncode != 0:
        print_status(Colors.YELLOW, "⚠️  pytest not found. Installing dependencies...")
        result = subprocess.run(["poetry", "install"], capture_output=True, text=True)
        if result.returncode != 0:
            print_status(Colors.RED, "❌ Failed to install dependencies")
            return False

    print_status(Colors.GREEN, "✅ Dependencies are ready!")
    return True


def test_python_version(version: str) -> bool:
    """Test with a specific Python version if available."""
    python_cmd = f"python{version}"

    # Check if the Python version is available
    try:
        subprocess.run(
            [python_cmd, "--version"], capture_output=True, text=True, check=True
        )

        print()
        print_status(Colors.BLUE, f"🐍 Testing with Python {version}...")

        # Run tests with this Python version
        command = ["poetry", "run", python_cmd, "-m", "pytest", "tests/", "-v"]
        success, _ = run_command(command, f"Python {version} Tests")

        if success:
            print_status(Colors.GREEN, f"✅ Python {version} tests passed!")
        else:
            print_status(
                Colors.YELLOW, f"⚠️  Python {version} tests failed or not available"
            )

        return success
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_status(Colors.YELLOW, f"⚠️  Python {version} not available")
        return False


def main() -> int:
    """Main test execution."""
    print("🧪 Running QuteWindow Test Suite")
    print("=" * 50)

    # Check prerequisites
    if not check_directory():
        return 1

    if not check_dependencies():
        return 1

    # Define test suites to run
    test_suites = [
        (
            "unit",
            ["poetry", "run", "pytest", "tests/", "-v", "--tb=short"],
            "Unit Tests",
        ),
        (
            "coverage",
            [
                "poetry",
                "run",
                "pytest",
                "tests/",
                "--cov=qutewindow",
                "--cov-report=term-missing",
                "--cov-report=html",
            ],
            "Coverage Tests",
        ),
        (
            "integration",
            ["poetry", "run", "pytest", "tests/", "-m", "integration", "-v"],
            "Integration Tests",
        ),
    ]

    # Track overall success
    overall_success = True

    # Run test suites
    for test_type, command, description in test_suites:
        success, _ = run_command(command, description)

        if success:
            print_status(Colors.GREEN, f"✅ {description} passed!")
        else:
            print_status(Colors.RED, f"❌ {description} failed!")
            overall_success = False

    # Test with different Python versions
    python_versions = ["3.9", "3.10", "3.11"]
    for version in python_versions:
        test_python_version(version)

    # Summary
    print()
    print("=" * 50)
    if overall_success:
        print_status(Colors.GREEN, "🎉 All test suites completed!")
        print()
        print("📊 Test Results Summary:")
        print("   - Unit Tests: ✅")
        print("   - Coverage: ✅")
        print("   - Integration Tests: ✅")
        print()
        print("📈 Coverage report generated in: htmlcov/index.html")
        return 0
    else:
        print_status(Colors.RED, "❌ Some test suites failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
