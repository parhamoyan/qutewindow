# Contributing to QuteWindow

We welcome contributions to QuteWindow! This guide will help you get started with contributing to the project.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git
- A GitHub account

### Development Setup

1. **Fork the Repository**

   Fork the QuteWindow repository on GitHub:
   https://github.com/parhamoyan/qutewindow

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/qutewindow.git
   cd qutewindow
   ```

3. **Set Up Virtual Environment**

   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

4. **Install Development Dependencies**

   ```bash
   pip install -e ".[dev]"
   ```

5. **Set Up Git Hooks**

   ```bash
   pre-commit install
   ```

6. **Set Up Upstream Remote**

   ```bash
   git remote add upstream https://github.com/parhamoyan/qutewindow.git
   ```

## Code Style and Quality

We maintain high code quality standards using several tools:

### Code Formatting

- **Black**: Code formatter
- **isort**: Import sorter

Format your code before committing:

```bash
black .
isort .
```

### Linting

- **flake8**: Code linter

Check your code for issues:

```bash
flake8 qutewindow/
```

### Type Checking

- **mypy**: Static type checker

Run type checking:

```bash
mypy qutewindow/
```

### Pre-commit Hooks

We use pre-commit hooks to ensure code quality:

```bash
# Run all hooks manually
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files
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

3. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

## Testing

### Running Tests

Run the test suite:

```bash
pytest
```

### Running Tests with Coverage

```bash
pytest --cov=qutewindow
```

### Writing Tests

We use pytest for testing. Here's an example test:

```python
import pytest
from qutewindow import QuteWindow
from PySide6.QtWidgets import QApplication

@pytest.fixture
def app():
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
    app.quit()

def test_qute_window_creation(app):
    window = QuteWindow()
    assert window is not None
    assert window.windowTitle() == ""

def test_qute_window_title(app):
    window = QuteWindow()
    window.setWindowTitle("Test Window")
    assert window.windowTitle() == "Test Window"
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

1. **Environment**: Python version, OS, QuteWindow version
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

## Recognition

Contributors will be recognized in:

- **README.md**: Listed in contributors section
- **CHANGELOG.md**: Credited for their contributions
- **Release Notes**: Mentioned in relevant release notes

Thank you for contributing to QuteWindow! 🎉