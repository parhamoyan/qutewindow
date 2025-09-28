# Agent Guidelines for CuteWindow

## Build/Lint/Test Commands
- **Run single test**: `poetry run pytest tests/test_basic.py::test_import -v`
- **Run all tests**: `poetry run pytest`
- **Format code**: `poetry run format-code` or `poetry run black . && poetry run isort .`
- **Lint code**: `poetry run flake8 cutewindow/`
- **Type check**: `poetry run mypy cutewindow/`
- **Quality check**: `poetry run python scripts/quality_check.py`

## Code Style Guidelines
- **Formatting**: Black with 88 character line length
- **Imports**: isort with black profile, group first-party/third-party
- **Types**: Strict mypy with type annotations required
- **Naming**: snake_case for functions/variables, PascalCase for classes
- **Docstrings**: Google-style with triple quotes
- **Error handling**: Use specific exceptions, avoid bare except
- **Platform code**: Separate implementations in platforms/ directory

## AI Subagents

### commit-agent
**Purpose**: Handles conventional commits for the CuteWindow project

**Description**: Specialized agent that follows the Conventional Commits specification to create properly formatted commit messages. Analyzes changes and categorizes them into appropriate commit types (feat, fix, docs, style, refactor, test, chore, etc.).

**Usage**: 
- Use when you need to commit changes following conventional commits standards
- Automatically determines commit type based on changes
- Ensures commit messages follow the format: `<type>(<scope>): <description>`
- Handles commit creation and pushing to GitHub

**Conventional Commits Types**:
- `feat`: New feature or functionality
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting, styling changes
- `refactor`: Code refactoring without functionality changes
- `test`: Test additions or modifications
- `chore`: Maintenance tasks, dependency updates
- `ci`: CI/CD configuration changes
- `build`: Build system or dependency changes

**Example Usage**:
```
Task(description="Commit documentation changes", prompt="Analyze the current git changes and create a conventional commit message. Then commit the changes and push to GitHub.", subagent_type="commit-agent")
```