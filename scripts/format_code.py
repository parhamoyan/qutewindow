#!/usr/bin/env python3
"""
Auto-format code to match style guidelines.

This script runs Black and isort to format code and sort imports.
"""

import subprocess
import sys
from pathlib import Path


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


def run_command(command: list[str], description: str) -> bool:
    """Run a command and return success status."""
    print_status(Colors.BLUE, f"Running {description}...")
    print(f"Command: {' '.join(command)}")

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        if result.returncode == 0:
            print_status(Colors.GREEN, f"✅ {description} completed successfully!")
            return True
        else:
            print_status(Colors.RED, f"❌ {description} failed!")
            return False
    except Exception as e:
        print(f"Error running command: {e}", file=sys.stderr)
        return False


def check_directory() -> bool:
    """Check if we're in the project root directory."""
    if not Path("pyproject.toml").exists():
        print_status(
            Colors.RED,
            "❌ Error: Please run this script from the project root directory",
        )
        return False
    return True


def main() -> int:
    """Main formatting execution."""
    print("🎨 Auto-formatting code...")
    print("=" * 50)

    # Check prerequisites
    if not check_directory():
        return 1

    # Track overall success
    overall_success = True

    # Run Black formatter
    if not run_command(["poetry", "run", "black", "."], "Black formatter"):
        overall_success = False

    print()

    # Run isort for import sorting
    if not run_command(["poetry", "run", "isort", "."], "Import sorting"):
        overall_success = False

    # Summary
    print()
    print("=" * 50)
    if overall_success:
        print_status(Colors.GREEN, "✅ Code formatting complete!")
        print()
        print(
            "Run 'poetry run pre-commit run --all-files' "
            "to check if all issues are resolved."
        )
        return 0
    else:
        print_status(Colors.RED, "❌ Code formatting encountered issues!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
