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