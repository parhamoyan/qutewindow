#!/bin/bash

# Comprehensive quality check script for QuteWindow

set -e  # Exit on any error

echo "🔍 Running QuteWindow Quality Checks"
echo "====================================="

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

# Function to run a check and report result
run_check() {
    local check_name="$1"
    local command="$2"
    local description="$3"

    echo ""
    print_status $BLUE "Running $description..."
    echo "Command: $command"
    echo "----------------------------------------"

    if eval $command; then
        print_status $GREEN "✅ $check_name passed!"
        return 0
    else
        print_status $RED "❌ $check_name failed!"
        echo ""
        print_status $YELLOW "💡 To fix $check_name issues:"
        case $check_name in
            "Black Formatting")
                echo "   Run: poetry run black ."
                echo "   Or: ./format-code.sh"
                ;;
            "Import Sorting")
                echo "   Run: poetry run isort ."
                echo "   Or: ./format-code.sh"
                ;;
            "Flake8 Linting")
                echo "   Check the output above for specific issues"
                echo "   Fix unused imports, style issues manually"
                ;;
            "Type Checking")
                echo "   Add missing type annotations"
                echo "   Check mypy errors in the output"
                ;;
            "Security Scan")
                echo "   Review and fix security issues"
                echo "   Check bandit report for details"
                ;;
            "Dependency Safety")
                echo "   Update vulnerable dependencies"
                echo "   Run: poetry update"
                ;;
        esac
        return 1
    fi
}

# Function to check if we're in the right directory
check_directory() {
    if [ ! -f "pyproject.toml" ]; then
        print_status $RED "❌ Error: Please run this script from the project root directory"
        exit 1
    fi
}

# Function to check dependencies
check_dependencies() {
    print_status $BLUE "📦 Checking dependencies..."

    local missing_deps=()

    for dep in black isort flake8 mypy bandit safety pytest; do
        if ! poetry show $dep > /dev/null 2>&1; then
            missing_deps+=($dep)
        fi
    done

    if [ ${#missing_deps[@]} -gt 0 ]; then
        print_status $YELLOW "⚠️  Missing dependencies: ${missing_deps[*]}"
        print_status $BLUE "📥 Installing missing dependencies..."
        poetry install
    fi

    print_status $GREEN "✅ Dependencies are ready!"
}

# Main quality check execution
main() {
    echo "🚀 Starting quality checks..."

    # Check directory
    check_directory

    # Check dependencies
    check_dependencies

    # Track overall success
    local overall_success=0

    # Run individual checks
    run_check "Black Formatting" \
              "poetry run black --check ." \
              "Code Formatting Check" || overall_success=1

    run_check "Import Sorting" \
              "poetry run isort --check-only ." \
              "Import Sorting Check" || overall_success=1

    run_check "Flake8 Linting" \
              "poetry run flake8 qutewindow/ tests/ --exclude=venv,.venv,build,dist,docs,examples,.*_rc\.py,compile_rcc\.py,conf\.py" \
              "Code Linting" || overall_success=1

    run_check "Type Checking" \
              "poetry run mypy qutewindow/ tests/ --ignore-missing-imports --no-strict-optional" \
              "Type Checking" || overall_success=1

    run_check "Security Scan" \
              "poetry run bandit -r qutewindow/ --skip=B101" \
              "Security Scanning" || overall_success=1

    run_check "Dependency Safety" \
              "poetry run safety check" \
              "Dependency Safety Check" || overall_success=1

    # Summary
    echo ""
    echo "====================================="
    if [ $overall_success -eq 0 ]; then
        print_status $GREEN "🎉 All quality checks passed!"
        echo ""
        echo "📊 Quality Check Results:"
        echo "   ✅ Code Formatting: Black"
        echo "   ✅ Import Sorting: isort"
        echo "   ✅ Code Linting: Flake8"
        echo "   ✅ Type Checking: MyPy"
        echo "   ✅ Security Scan: Bandit"
        echo "   ✅ Dependency Safety: Safety"
        echo ""
        echo "🚀 Your code is ready for commit!"
    else
        print_status $RED "❌ Some quality checks failed!"
        echo ""
        echo "📊 Quality Check Results:"
        echo "   ❌ Code Formatting: Black (fixable)"
        echo "   ❌ Import Sorting: isort (fixable)"
        echo "   ❌ Code Linting: Flake8 (manual fix required)"
        echo "   ❌ Type Checking: MyPy (manual fix required)"
        echo "   ❌ Security Scan: Bandit (review required)"
        echo "   ❌ Dependency Safety: Safety (update required)"
        echo ""
        print_status $YELLOW "💡 Fix the issues above and run this script again"
        print_status $YELLOW "💡 Use ./format-code.sh for auto-fixable issues"
        exit 1
    fi
}

# Run main function
main "$@"
