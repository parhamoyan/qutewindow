#!/bin/bash

# Comprehensive test runner script for QuteWindow

set -e  # Exit on any error

echo "🧪 Running QuteWindow Test Suite"
echo "================================="

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Function to run tests with different options
run_tests() {
    local test_type="$1"
    local test_args="$2"
    local description="$3"

    echo ""
    echo "🔍 Running $description..."
    echo "Command: poetry run pytest $test_args"
    echo "----------------------------------------"

    if poetry run pytest $test_args; then
        echo "✅ $description passed!"
    else
        echo "❌ $description failed!"
        return 1
    fi
}

# Function to check if dependencies are installed
check_dependencies() {
    echo "📦 Checking dependencies..."

    if ! poetry show pytest > /dev/null 2>&1; then
        echo "❌ pytest not found. Installing dependencies..."
        poetry install
    fi

    echo "✅ Dependencies are ready!"
}

# Main test execution
main() {
    echo "🚀 Starting test execution..."

    # Check dependencies
    check_dependencies

    # Run different test suites
    run_tests "unit" "tests/ -v --tb=short" "Unit Tests"

    run_tests "coverage" "tests/ --cov=qutewindow --cov-report=term-missing --cov-report=html" "Coverage Tests"

    run_tests "integration" "tests/ -m integration -v" "Integration Tests"

    # Run tests with different Python versions if available
    if command -v python3.9 &> /dev/null; then
        echo ""
        echo "🐍 Testing with Python 3.9..."
        poetry run python3.9 -m pytest tests/ -v || echo "⚠️  Python 3.9 tests failed or not available"
    fi

    if command -v python3.10 &> /dev/null; then
        echo ""
        echo "🐍 Testing with Python 3.10..."
        poetry run python3.10 -m pytest tests/ -v || echo "⚠️  Python 3.10 tests failed or not available"
    fi

    if command -v python3.11 &> /dev/null; then
        echo ""
        echo "🐍 Testing with Python 3.11..."
        poetry run python3.11 -m pytest tests/ -v || echo "⚠️  Python 3.11 tests failed or not available"
    fi

    echo ""
    echo "🎉 All test suites completed!"
    echo ""
    echo "📊 Test Results Summary:"
    echo "   - Unit Tests: ✅"
    echo "   - Coverage: ✅"
    echo "   - Integration Tests: ✅"
    echo ""
    echo "📈 Coverage report generated in: htmlcov/index.html"
}

# Run main function
main "$@"
