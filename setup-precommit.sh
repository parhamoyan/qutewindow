#!/bin/bash

# Setup pre-commit hooks for QuteWindow project

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}📋 $message${NC}"
}

# Function to check if we're in the right directory
check_directory() {
    if [ ! -f "pyproject.toml" ]; then
        print_status $RED "❌ Error: Please run this script from the project root directory"
        exit 1
    fi
}

# Function to check if Poetry is installed
check_poetry() {
    if ! command -v poetry &> /dev/null; then
        print_status $RED "❌ Error: Poetry is not installed"
        print_status $YELLOW "💡 Please install Poetry first:"
        echo "   curl -sSL https://install.python-poetry.org | python3 -"
        echo "   Or: pip install poetry"
        exit 1
    fi
}

# Function to install pre-commit if not already installed
install_precommit() {
    print_status $BLUE "📦 Checking pre-commit installation..."

    if ! poetry show pre-commit > /dev/null 2>&1; then
        print_status $BLUE "📥 Installing pre-commit..."
        if poetry add --group dev pre-commit; then
            print_status $GREEN "✅ Pre-commit installed successfully!"
        else
            print_status $RED "❌ Failed to install pre-commit"
            exit 1
        fi
    else
        print_status $GREEN "✅ Pre-commit is already installed"
    fi
}

# Function to install pre-commit hooks
install_hooks() {
    print_status $BLUE "⚙️  Installing pre-commit hooks..."

    # Install standard pre-commit hooks
    if poetry run pre-commit install; then
        print_status $GREEN "✅ Pre-commit hooks installed successfully!"
    else
        print_status $RED "❌ Failed to install pre-commit hooks"
        exit 1
    fi

    # Install commit-msg hook (optional, for commit message validation)
    print_status $BLUE "📝 Installing commit message hook..."
    if poetry run pre-commit install --hook-type commit-msg; then
        print_status $GREEN "✅ Commit message hook installed successfully!"
    else
        print_status $YELLOW "⚠️  Commit message hook installation failed (this is optional)"
    fi
}

# Function to verify installation
verify_installation() {
    print_status $BLUE "🔍 Verifying pre-commit installation..."

    if poetry run pre-commit --version > /dev/null 2>&1; then
        print_status $GREEN "✅ Pre-commit verification successful!"
        return 0
    else
        print_status $RED "❌ Pre-commit verification failed"
        return 1
    fi
}

# Main setup function
main() {
    echo "🔧 Setting up pre-commit hooks for QuteWindow"
    echo "=========================================="

    # Check prerequisites
    check_directory
    check_poetry

    # Install pre-commit and hooks
    install_precommit
    install_hooks

    # Verify installation
    if verify_installation; then
        echo ""
        print_status $GREEN "🎉 Pre-commit setup complete!"
        echo ""
        echo "📖 Usage Information:"
        echo "   • Pre-commit will run automatically on each commit"
        echo "   • To run manually on all files: poetry run pre-commit run --all-files"
        echo "   • To update hooks: poetry run pre-commit autoupdate"
        echo "   • To skip hooks (not recommended): git commit --no-verify"
        echo ""
        echo "🔧 Troubleshooting:"
        echo "   • If hooks fail, run: poetry run pre-commit run --all-files"
        echo "   • To fix formatting: ./format-code.sh"
        echo "   • For quality checks: ./scripts/quality_check.sh"
        echo ""
        print_status $GREEN "✅ You're all set for development!"
    else
        print_status $RED "❌ Pre-commit setup encountered issues"
        echo ""
        print_status $YELLOW "💡 Please check the error messages above and try again"
        exit 1
    fi
}

# Run main function
main "$@"
