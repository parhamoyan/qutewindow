#!/usr/bin/env python3
"""
Comprehensive quality check script for QuteWindow.

This script runs various code quality checks including formatting,
linting, type checking, and security scanning.
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
    """Check if required dependencies are installed."""
    print_status(Colors.BLUE, "📦 Checking dependencies...")

    required_deps = ["black", "isort", "flake8", "mypy", "bandit", "safety"]
    missing_deps = []

    for dep in required_deps:
        result = subprocess.run(["poetry", "show", dep], capture_output=True, text=True)
        if result.returncode != 0:
            missing_deps.append(dep)

    if missing_deps:
        print_status(
            Colors.YELLOW, f"⚠️  Missing dependencies: {', '.join(missing_deps)}"
        )
        print_status(Colors.BLUE, "📥 Installing missing dependencies...")
        result = subprocess.run(["poetry", "install"], capture_output=True, text=True)
        if result.returncode != 0:
            print_status(Colors.RED, "❌ Failed to install dependencies")
            return False

    print_status(Colors.GREEN, "✅ Dependencies are ready!")
    return True


def get_fix_suggestions(check_name: str) -> List[str]:
    """Get fix suggestions for failed checks."""
    suggestions = {
        "Black Formatting": [
            "   Run: poetry run black .",
            "   Or: poetry run format-code",
        ],
        "Import Sorting": [
            "   Run: poetry run isort .",
            "   Or: poetry run format-code",
        ],
        "Flake8 Linting": [
            "   Check the output above for specific issues",
            "   Fix unused imports, style issues manually",
        ],
        "Type Checking": [
            "   Add missing type annotations",
            "   Check mypy errors in the output",
        ],
        "Security Scan": [
            "   Review and fix security issues",
            "   Check bandit report for details",
        ],
        "Dependency Safety": [
            "   Update vulnerable dependencies",
            "   Run: poetry update",
        ],
    }
    return suggestions.get(check_name, ["   Review the output above for details"])


def main() -> int:
    """Main quality check execution."""
    print("🔍 Running QuteWindow Quality Checks")
    print("=" * 50)

    # Check prerequisites
    if not check_directory():
        return 1

    if not check_dependencies():
        return 1

    # Define checks to run
    checks = [
        (
            "Black Formatting",
            ["poetry", "run", "black", "--check", "."],
            "Code Formatting Check",
        ),
        (
            "Import Sorting",
            ["poetry", "run", "isort", "--check-only", "."],
            "Import Sorting Check",
        ),
        (
            "Flake8 Linting",
            [
                "poetry",
                "run",
                "flake8",
                "qutewindow/",
                "--exclude=venv,.venv,build,dist,docs,examples,"
                ".*_rc\\.py,compile_rcc\\.py,conf\\.py",
            ],
            "Code Linting",
        ),
        (
            "Type Checking",
            [
                "poetry",
                "run",
                "mypy",
                "qutewindow/",
                "--ignore-missing-imports",
                "--no-strict-optional",
            ],
            "Type Checking",
        ),
        (
            "Security Scan",
            ["poetry", "run", "bandit", "-r", "qutewindow/", "--skip=B101"],
            "Security Scanning",
        ),
        (
            "Dependency Safety",
            ["poetry", "run", "safety", "check"],
            "Dependency Safety Check",
        ),
    ]

    # Track overall success
    overall_success = True

    # Run individual checks
    for check_name, command, description in checks:
        success, _ = run_command(command, description)

        if success:
            print_status(Colors.GREEN, f"✅ {check_name} passed!")
        else:
            print_status(Colors.RED, f"❌ {check_name} failed!")
            print()
            print_status(Colors.YELLOW, f"💡 To fix {check_name} issues:")
            for suggestion in get_fix_suggestions(check_name):
                print(suggestion)
            overall_success = False

    # Summary
    print()
    print("=" * 50)
    if overall_success:
        print_status(Colors.GREEN, "🎉 All quality checks passed!")
        print()
        print("📊 Quality Check Results:")
        print("   ✅ Code Formatting: Black")
        print("   ✅ Import Sorting: isort")
        print("   ✅ Code Linting: Flake8")
        print("   ✅ Type Checking: MyPy")
        print("   ✅ Security Scan: Bandit")
        print("   ✅ Dependency Safety: Safety")
        print()
        print("🚀 Your code is ready for commit!")
        return 0
    else:
        print_status(Colors.RED, "❌ Some quality checks failed!")
        print()
        print("📊 Quality Check Results:")
        print("   ❌ Code Formatting: Black (fixable)")
        print("   ❌ Import Sorting: isort (fixable)")
        print("   ❌ Code Linting: Flake8 (manual fix required)")
        print("   ❌ Type Checking: MyPy (manual fix required)")
        print("   ❌ Security Scan: Bandit (review required)")
        print("   ❌ Dependency Safety: Safety (update required)")
        print()
        print_status(Colors.YELLOW, "💡 Fix the issues above and run this script again")
        print_status(
            Colors.YELLOW, "💡 Use poetry run format-code for auto-fixable issues"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
