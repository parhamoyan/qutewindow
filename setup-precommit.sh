#!/bin/bash

# Setup pre-commit hooks for QuteWindow project

echo "🔧 Setting up pre-commit hooks..."

# Install pre-commit
echo "📦 Installing pre-commit..."
poetry add --group dev pre-commit

# Install pre-commit hooks
echo "⚙️  Installing pre-commit hooks..."
poetry run pre-commit install

# Install pre-commit commit-msg hook (optional, for commit message validation)
echo "📝 Installing commit message hook..."
poetry run pre-commit install --hook-type commit-msg

echo "✅ Pre-commit setup complete!"
echo ""
echo "Pre-commit will now run automatically on each commit."
echo "To run pre-commit manually on all files:"
echo "  poetry run pre-commit run --all-files"
echo ""
echo "To update pre-commit hooks to latest versions:"
echo "  poetry run pre-commit autoupdate"
echo ""
echo "To skip pre-commit hooks (not recommended):"
echo "  git commit --no-verify"
