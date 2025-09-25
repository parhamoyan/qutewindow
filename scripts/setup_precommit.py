#!/usr/bin/env python3
"""
Setup pre-commit hooks for CuteWindow project.

This script installs and configures pre-commit hooks for the project.
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


def run_command(command: list[str], description: str, check: bool = True) -> bool:
    """Run a command and return success status."""
    print_status(Colors.BLUE, f"Running {description}...")

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=check)

        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)

        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}", file=sys.stderr)
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


def check_poetry() -> bool:
    """Check if Poetry is installed."""
    try:
        result = subprocess.run(
            ["poetry", "--version"], capture_output=True, text=True, check=True
        )
        print_status(Colors.GREEN, f"✅ Poetry found: {result.stdout.strip()}")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print_status(Colors.RED, "❌ Error: Poetry is not installed")
        print_status(Colors.YELLOW, "💡 Please install Poetry first:")
        print("   curl -sSL https://install.python-poetry.org | python3 -")
        print("   Or: pip install poetry")
        return False


def install_precommit() -> bool:
    """Install pre-commit if not already installed."""
    print_status(Colors.BLUE, "📦 Checking pre-commit installation...")

    # Check if pre-commit is already installed
    result = subprocess.run(
        ["poetry", "show", "pre-commit"], capture_output=True, text=True
    )

    if result.returncode != 0:
        print_status(Colors.BLUE, "📥 Installing pre-commit...")
        if not run_command(
            ["poetry", "add", "--group", "dev", "pre-commit"], "pre-commit installation"
        ):
            print_status(Colors.RED, "❌ Failed to install pre-commit")
            return False
        print_status(Colors.GREEN, "✅ Pre-commit installed successfully!")
    else:
        print_status(Colors.GREEN, "✅ Pre-commit is already installed")

    return True


def install_hooks() -> bool:
    """Install pre-commit hooks."""
    print_status(Colors.BLUE, "⚙️  Installing pre-commit hooks...")

    # Install standard pre-commit hooks
    if not run_command(
        ["poetry", "run", "pre-commit", "install"], "pre-commit hooks installation"
    ):
        print_status(Colors.RED, "❌ Failed to install pre-commit hooks")
        return False

    print_status(Colors.GREEN, "✅ Pre-commit hooks installed successfully!")

    # Install commit-msg hook (optional, for commit message validation)
    print_status(Colors.BLUE, "📝 Installing commit message hook...")
    if not run_command(
        ["poetry", "run", "pre-commit", "install", "--hook-type", "commit-msg"],
        "commit message hook installation",
        check=False,
    ):
        print_status(
            Colors.YELLOW,
            "⚠️  Commit message hook installation failed (this is optional)",
        )
    else:
        print_status(Colors.GREEN, "✅ Commit message hook installed successfully!")

    return True


def verify_installation() -> bool:
    """Verify pre-commit installation."""
    print_status(Colors.BLUE, "🔍 Verifying pre-commit installation...")

    if run_command(
        ["poetry", "run", "pre-commit", "--version"], "pre-commit verification"
    ):
        print_status(Colors.GREEN, "✅ Pre-commit verification successful!")
        return True
    else:
        print_status(Colors.RED, "❌ Pre-commit verification failed")
        return False


def main() -> int:
    """Main setup function."""
    print("🔧 Setting up pre-commit hooks for CuteWindow")
    print("=" * 50)

    # Check prerequisites
    if not check_directory():
        return 1

    if not check_poetry():
        return 1

    # Install pre-commit and hooks
    if not install_precommit():
        return 1

    if not install_hooks():
        return 1

    # Verify installation
    if verify_installation():
        print()
        print_status(Colors.GREEN, "🎉 Pre-commit setup complete!")
        print()
        print("📖 Usage Information:")
        print("   • Pre-commit will run automatically on each commit")
        print(
            "   • To run manually on all files: poetry run pre-commit run --all-files"
        )
        print("   • To update hooks: poetry run pre-commit autoupdate")
        print("   • To skip hooks (not recommended): git commit --no-verify")
        print()
        print("🔧 Troubleshooting:")
        print("   • If hooks fail, run: poetry run pre-commit run --all-files")
        print("   • To fix formatting: poetry run format-code")
        print("   • For quality checks: poetry run quality-check")
        print()
        print_status(Colors.GREEN, "✅ You're all set for development!")
        return 0
    else:
        print_status(Colors.RED, "❌ Pre-commit setup encountered issues")
        print()
        print_status(
            Colors.YELLOW, "💡 Please check the error messages above and try again"
        )
        return 1


if __name__ == "__main__":
    sys.exit(main())
