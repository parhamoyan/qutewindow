#!/bin/bash

# Auto-format code to match style guidelines

echo "🎨 Auto-formatting code..."

# Run black formatter
echo "⚫ Running black formatter..."
poetry run black .

# Run isort for import sorting
echo "📚 Running isort for import sorting..."
poetry run isort .

echo "✅ Code formatting complete!"
echo ""
echo "Run 'poetry run pre-commit run --all-files' to check if all issues are resolved."
