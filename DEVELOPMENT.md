# Development Guide

## 🚀 Getting Started

This project follows modern Python development best practices with comprehensive tooling for code quality, testing, and documentation.

### 📋 Prerequisites

- **Python**: 3.9 or higher
- **Poetry**: Dependency management (version 1.2+ recommended)
- **Git**: Version control
- **GitHub Account**: For contributions

### 🔧 Initial Setup

```bash
# Clone the repository
git clone https://github.com/parhamoyan/qutewindow.git
cd qutewindow

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install all dependencies including development dependencies
poetry install

# Set up pre-commit hooks
poetry run python scripts/setup_precommit.py

# Verify installation
poetry run python -c "import qutewindow; print('CuteWindow installed successfully')"
```

## 🪝 Pre-commit Setup

This project uses pre-commit hooks to ensure code quality and consistency before commits.

### ✅ Installation

Run the setup script to install and configure pre-commit hooks:

```bash
./setup-precommit.sh
```

### 🔧 Manual Installation

If you prefer to install manually:

```bash
# Install pre-commit
poetry add --group dev pre-commit

# Install the hooks
poetry run pre-commit install
```

### 🪝 Pre-commit Hooks

The following hooks are configured:

- **Black**: Code formatter (Python) - Auto-fixes formatting
- **isort**: Import sorter (Python) - Auto-fixes import ordering
- **Flake8**: Linter (Python) - Checks for style issues and unused imports
- **MyPy**: Type checker (Python) - Validates type annotations
- **Bandit**: Security linter (Python) - Checks for security issues
- **Basic hooks**: Trailing whitespace, YAML validation, file size checks, debug statements, etc.

### 🎯 Hook Configuration

Hooks are configured in `.pre-commit-config.yaml` with the following settings:
- Black: Line length 88, Python 3
- isort: Black profile, line length 88
- Flake8: Max line length 88, ignores E203 and W503
- MyPy: Ignores missing imports, no strict optional
- Bandit: Skips B101 (assert statements)

### 🚀 Usage

**Automatic**: Pre-commit hooks run automatically on each `git commit`.

**Manual check**: Run pre-commit on all files:
```bash
poetry run pre-commit run --all-files
```

**Update hooks**: Update to latest versions:
```bash
poetry run pre-commit autoupdate
```

**Skip hooks** (not recommended):
```bash
git commit --no-verify
```

### 🎨 Code Formatting

If formatting issues are found, you can fix them automatically:

```bash
# Using individual tools
poetry run black .
poetry run isort .

# Using convenience script
poetry run python scripts/format_code.py
```

## 🧪 Testing

### Running Tests

```bash
# Run all tests
poetry run pytest

# Run tests with coverage
poetry run pytest --cov=qutewindow --cov-report=term-missing --cov-report=html

# Run specific test file
poetry run pytest tests/test_qutewindow.py

# Run tests with verbose output
poetry run pytest -v

# Run tests with markers
poetry run pytest -m unit          # Unit tests only
poetry run pytest -m integration   # Integration tests only
poetry run pytest -m "not slow"    # Exclude slow tests
```

### Test Scripts

```bash
# Comprehensive test runner (recommended)
poetry run python scripts/run_tests.py

# Quick test run
poetry run pytest tests/ -v

# Run tests with coverage report
poetry run pytest --cov=qutewindow --cov-report=html
open htmlcov/index.html  # View coverage report
```

### Test Configuration

Tests are configured in `pytest.ini` with the following settings:
- Test paths: `tests/`
- Python files: `test_*.py`
- Verbose output with short tracebacks
- Color output and duration reporting
- Custom markers: `slow`, `integration`, `unit`

### Writing Tests

- Use `pytest` for testing
- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Mock external dependencies when necessary

Example:
```python
def test_window_creation(qapp):
    """Test basic window creation."""
    from qutewindow import CuteWindow

    window = CuteWindow()
    assert window is not None
    window.close()
```

## 🔍 Quality Assurance

### Quality Check Script

Run comprehensive quality checks:

```bash
poetry run python scripts/quality_check.py
```

This script runs:
- ✅ Code formatting (Black)
- ✅ Import sorting (isort)
- ✅ Code linting (Flake8)
- ✅ Type checking (MyPy)
- ✅ Security scanning (Bandit)
- ✅ Dependency safety (Safety)

The script provides:
- Colored output for easy reading
- Detailed error messages
- Specific fix commands for each type of issue
- Automatic dependency checking and installation
- Overall success/failure summary

### Individual Quality Checks

```bash
# Code formatting
poetry run black --check .

# Import sorting
poetry run isort --check-only .

# Linting
poetry run flake8 qutewindow/ tests/

# Type checking
poetry run mypy qutewindow/ tests/

# Security scan
poetry run bandit -r qutewindow/

# Dependency safety
poetry run safety check
```

## 📚 Documentation

### Building Documentation

```bash
# Build HTML documentation
cd docs
make html

# View documentation
open docs/_build/html/index.html
```

### Documentation Structure

- **README.md**: Project overview and quick start
- **CONTRIBUTING.md**: Contribution guidelines
- **DEVELOPMENT.md**: Development guide (this file)
- **docs/**: Comprehensive documentation with Sphinx
- **CHANGELOG.md**: Version history and changes
- **SECURITY.md**: Security policy and reporting
- **CODE_OF_CONDUCT.md**: Community guidelines

## 🔄 CI/CD Integration

The same tools run in CI/CD pipelines. If formatting checks fail, the pipeline will show commands to fix the issues locally and will not fail the build but provide helpful guidance.

### GitHub Actions

- **CI Pipeline**: `.github/workflows/ci.yml`
- **Quality Pipeline**: `.github/workflows/quality.yml`
- **Documentation Pipeline**: `.github/workflows/docs.yml`
- **Coverage Pipeline**: `.github/workflows/coverage.yml`

### Quality Gates

- ✅ Code formatting must pass
- ✅ Tests must pass on all supported Python versions
- ✅ Security scans must pass
- ✅ Documentation must build successfully
- ⚠️ Linting and type checking provide guidance but don't block

## 🛠️ Troubleshooting

### Pre-commit Issues

If pre-commit hooks fail:
1. **Auto-fixable issues** (Black, isort): Run `./format-code.sh` or individual commands
2. **Linting issues** (Flake8): Fix unused imports, style issues manually
3. **Type issues** (MyPy): Add missing type annotations
4. **Security issues** (Bandit): Review and address security concerns

After fixing issues:
```bash
# Verify all fixes
poetry run pre-commit run --all-files
# Commit again
git commit -m "Your message"
```

### Common Issues

**Import Errors**:
```bash
# Ensure dependencies are installed
poetry install

# Check Python path
poetry run python -c "import qutewindow"
```

**Test Failures**:
```bash
# Run tests with verbose output
poetry run pytest -v --tb=long

# Run specific failing test
poetry run pytest tests/test_file.py::test_function
```

**Type Checking Errors**:
```bash
# Run mypy with detailed output
poetry run mypy qutewindow/ --show-error-codes --pretty
```

## 📋 Current Code Quality Status

The pre-commit hooks will catch:
- ✅ Trailing whitespace and file ending issues
- ✅ Code formatting (Black)
- ✅ Import sorting (isort)
- ⚠️ Unused imports (Flake8 F401) - Needs manual cleanup
- ⚠️ Line length issues (Flake8 E501) - Needs manual attention
- ⚠️ Type annotations (MyPy) - Needs completion
- ✅ Security issues (Bandit) - Excludes test assertions (B101)

## 🎯 Development Workflow

### 1. Feature Development

```bash
# Create feature branch
git checkout -b feature/amazing-feature

# Make changes
# ... code changes ...

# Run quality checks
./scripts/quality_check.sh

# Run tests
./scripts/run_tests.sh

# Commit changes
git add .
git commit -m "feat: add amazing feature"

# Push branch
git push origin feature/amazing-feature
```

### 2. Bug Fixing

```bash
# Create bugfix branch
git checkout -b fix/annoying-bug

# Make fixes
# ... bug fixes ...

# Run quality checks
./scripts/quality_check.sh

# Run tests
./scripts/run_tests.sh

# Commit changes
git add .
git commit -m "fix: resolve annoying bug"

# Push branch
git push origin fix/annoying-bug
```

### 3. Release Preparation

```bash
# Update version
poetry version patch/minor/major

# Update changelog
# Edit CHANGELOG.md

# Run final quality checks
./scripts/quality_check.sh

# Run full test suite
./scripts/run_tests.sh

# Commit and tag
git add .
git commit -m "release: prepare version X.Y.Z"
git tag v.X.Y.Z

# Push
git push origin main --tags
```

## 📚 For More Information

- [pre-commit documentation](https://pre-commit.com/)
- [Black formatter](https://black.readthedocs.io/)
- [isort import sorter](https://pycqa.github.io/isort/)
- [Flake8 linter](https://flake8.pycqa.org/)
- [MyPy type checker](https://mypy.readthedocs.io/)
- [Bandit security linter](https://bandit.readthedocs.io/)
- [pytest testing framework](https://docs.pytest.org/)
- [Poetry dependency management](https://python-poetry.org/)
