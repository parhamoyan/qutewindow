# Contributing to CuteWindow

We welcome contributions to CuteWindow! This guide will help you get started with contributing to the project.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Poetry (dependency management)
- Git
- A GitHub account

### Development Setup

1. **Fork the Repository**

   Fork the CuteWindow repository on GitHub:
   https://github.com/parhamoyan/cutewindow

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/cutewindow.git
   cd cutewindow
   ```

3. **Install Dependencies with Poetry**

   ```bash
   # Install all dependencies including development dependencies
   poetry install

   # Or install with development dependencies explicitly
   poetry install --with dev
   ```

4. **Set Up Git Hooks**

   ```bash
# Use the provided setup script
poetry run python scripts/setup_precommit.py

# Or install manually
poetry run pre-commit install
   ```

5. **Set Up Upstream Remote**

   ```bash
   git remote add upstream https://github.com/parhamoyan/cutewindow.git
   ```

## Code Style and Quality

We maintain high code quality standards using several tools:

### Code Formatting

- **Black**: Code formatter
- **isort**: Import sorter

Format your code before committing:

```bash
# Using Poetry
poetry run black .
poetry run isort .

# Or use the convenience script
poetry run python scripts/format_code.py
```

### Linting

- **flake8**: Code linter

Check your code for issues:

```bash
poetry run flake8 cutewindow/
```

### Type Checking

- **mypy**: Static type checker

Run type checking:

```bash
poetry run mypy cutewindow/
```

### Security Scanning

- **bandit**: Security linter
- **safety**: Dependency safety checker

Run security checks:

```bash
poetry run bandit -r cutewindow/
poetry run safety check
```

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

```bash
# Run all hooks manually
poetry run pre-commit run --all-files

# Run specific hook
poetry run pre-commit run black --all-files

# Update hooks to latest versions
poetry run pre-commit autoupdate
```

## Making Changes

### Creating a Branch

Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/your-fix-name
```

### Making Your Changes

1. **Write Code**: Implement your feature or fix
2. **Add Tests**: Write tests for your changes
3. **Update Documentation**: Update relevant documentation
4. **Follow Code Style**: Ensure your code follows our style guidelines

### Quality Checks

Before committing, run quality checks:

```bash
# Run comprehensive quality checks
poetry run python scripts/quality_check.py

# Or run individual checks
poetry run black --check .
poetry run isort --check-only .
poetry run flake8 cutewindow/
poetry run mypy cutewindow/
```

### Committing Your Changes

1. **Stage Your Changes**

   ```bash
   git add .
   ```

2. **Create a Commit**

   Use a clear and descriptive commit message:

   ```bash
   git commit -m "feat: add new window animation feature"
   ```

   We follow the [Conventional Commits](https://www.conventionalcommits.org/) format:

   - `feat:`: New feature
   - `fix:`: Bug fix
   - `docs:`: Documentation changes
   - `style:`: Code style changes
   - `refactor:`: Code refactoring
   - `test:`: Test changes
   - `chore:`: Maintenance tasks

   **Note**: Pre-commit hooks will run automatically and may fix formatting issues or report problems.

3. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

## Testing

### Running Tests

Run the test suite:

```bash
# Using Poetry
poetry run pytest

# Or use the convenience script
poetry run python scripts/run_tests.py
```

### Running Tests with Coverage

```bash
poetry run pytest --cov=cutewindow --cov-report=term-missing
```

### Running Specific Tests

```bash
# Run specific test file
poetry run pytest tests/test_cutewindow.py

# Run with verbose output
poetry run pytest -v

# Run specific test function
poetry run pytest tests/test_cutewindow.py::test_window_creation
```

### Writing Tests

We use pytest for testing. Here's an example test:

```python
import pytest
from cutewindow import CuteWindow
from PySide6.QtWidgets import QApplication

@pytest.fixture
def qapp():
    """Fixture to provide QApplication instance."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()

def test_window_creation(qapp):
    """Test basic window creation."""
    window = CuteWindow()
    assert window is not None
    assert window.windowTitle() == ""
    window.close()

def test_window_title(qapp):
    """Test window title setting."""
    window = CuteWindow()
    window.setWindowTitle("Test Window")
    assert window.windowTitle() == "Test Window"
    window.close()
```

## Documentation

### Building Documentation

Build the documentation:

```bash
cd docs
make html
```

### Viewing Documentation

Open the built documentation:

```bash
open docs/_build/html/index.html
```

### Updating Documentation

When adding new features or making changes:

1. Update relevant docstrings
2. Add or update API documentation
3. Add or update examples
4. Update the README if necessary

## Pull Request Process

### Creating a Pull Request

1. **Ensure Your Branch is Up to Date**

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push Your Changes**

   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create Pull Request**

   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your branch and the upstream main branch
   - Fill in the PR template
   - Submit the PR

### Pull Request Template

Use the following template for your pull request:

```markdown
## Description
[Describe your changes in detail]

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
[Describe how you tested your changes]

## Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
```

### Review Process

1. **Automated Checks**: Your PR will run automated checks (tests, linting, etc.)
2. **Code Review**: Maintainers will review your code
3. **Feedback**: Address any feedback from reviewers
4. **Approval**: Once approved, your PR will be merged

## Reporting Issues

### Bug Reports

When reporting bugs, please include:

1. **Environment**: Python version, OS, CuteWindow version
2. **Steps to Reproduce**: Clear steps to reproduce the issue
3. **Expected Behavior**: What you expected to happen
4. **Actual Behavior**: What actually happened
5. **Error Messages**: Any error messages or stack traces

### Feature Requests

For feature requests, please include:

1. **Description**: Clear description of the feature
2. **Use Case**: Why this feature is needed
3. **Proposed Solution**: How you envision the feature working
4. **Alternatives**: Any alternative solutions you considered

## Community Guidelines

### Code of Conduct

Be respectful and inclusive:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For general questions and discussions
- **Documentation**: Check the docs first
- **Existing Issues**: Search before creating new issues

## Troubleshooting

### Common Issues and Solutions

#### Poetry Installation Issues

**Problem**: Poetry is not installed or not found
```bash
# Install Poetry using the official installer
curl -sSL https://install.python-poetry.org | python3 -

# Or using pip
pip install poetry
```

**Problem**: Dependencies fail to install
```bash
# Update Poetry and try again
poetry self update
poetry lock
poetry install

# Clear cache and reinstall
poetry cache clear --all pypi
poetry install
```

#### Pre-commit Hook Issues

**Problem**: Pre-commit hooks fail
```bash
# Run hooks manually to see specific errors
poetry run pre-commit run --all-files

# Auto-fix formatting issues
poetry run python scripts/format_code.py

# Update hooks to latest versions
poetry run pre-commit autoupdate
```

**Problem**: Want to skip hooks (not recommended)
```bash
git commit --no-verify
```

#### Test Failures

**Problem**: Tests fail with import errors
```bash
# Ensure dependencies are installed
poetry install

# Check if cutewindow can be imported
poetry run python -c "import cutewindow; print('Import successful')"
```

**Problem**: Tests fail with Qt/display issues
```bash
# Run tests without display (for CI environments)
export QT_QPA_PLATFORM=offscreen
poetry run pytest

# Or run with virtual display on Linux
sudo apt-get install xvfb
xvfb-run -a poetry run pytest
```

#### Type Checking Issues

**Problem**: MyPy reports type errors
```bash
# Run MyPy with detailed output
poetry run mypy cutewindow/ --show-error-codes --pretty

# Check specific file
poetry run mypy cutewindow/windows/CuteWindow.py
```

#### Code Quality Issues

**Problem**: Quality checks fail
```bash
# Run comprehensive quality check
./scripts/quality_check.sh

# Fix formatting automatically
./format-code.sh

# Check specific issues
poetry run flake8 cutewindow/ --statistics
```

### Getting Help

If you encounter issues not covered here:

1. **Check existing issues**: Search GitHub Issues for similar problems
2. **Create a new issue**: Provide detailed information about your problem
3. **Join discussions**: Ask questions in GitHub Discussions
4. **Check documentation**: Review the latest documentation

## Recognition

Contributors will be recognized in:

- **README.md**: Listed in contributors section
- **CHANGELOG.md**: Credited for their contributions
- **Release Notes**: Mentioned in relevant release notes

Thank you for contributing to CuteWindow! 🎉
