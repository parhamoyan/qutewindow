# Release Guide

This guide explains how to release new versions of CuteWindow to PyPI and GitHub.

## Overview

CuteWindow uses an automated release process that handles:
- Building the package
- Running tests and quality checks
- Publishing to PyPI
- Creating GitHub releases
- Generating changelog notes

## Prerequisites

Before creating a release, ensure you have:

1. **PyPI API Token**: Set up as a repository secret named `PYPI_API_TOKEN`
2. **GitHub Repository Permissions**: Write access to create releases
3. **Clean Working Directory**: No uncommitted changes

## Release Methods

### Method 1: Automated Tag-based Release (Recommended)

This is the preferred method for releases.

#### Steps:

1. **Update Version in pyproject.toml**
   ```toml
   [tool.poetry]
   version = "0.3.0"  # Update to new version
   ```

2. **Update CHANGELOG.md**
   ```markdown
   ## [0.3.0] - 2024-09-24

   ### Added
   - New feature X
   - Improvement Y

   ### Changed
   - Updated dependency Z

   ### Fixed
   - Bug fix A
   ```

3. **Commit Changes**
   ```bash
   git add pyproject.toml CHANGELOG.md
   git commit -m "chore: prepare release v0.3.0"
   git push origin main
   ```

4. **Create and Push Tag**
   ```bash
   git tag v0.3.0
   git push origin v0.3.0
   ```

5. **Monitor Release**
   - Go to Actions tab in GitHub
   - Watch the "Release" workflow run
   - Check for any failures

### Method 2: Manual Release via GitHub Actions

Use this method for special cases or testing.

#### Steps:

1. **Go to GitHub Actions**
   - Navigate to your repository
   - Click on "Actions" tab
   - Select "Release" workflow

2. **Run Workflow**
   - Click "Run workflow"
   - Fill in the parameters:
     - **Version**: e.g., `0.3.0`
     - **Prerelease**: Check if this is a prerelease

3. **Monitor Progress**
   - Watch the workflow execution
   - Check logs for any issues

### Method 3: Local Release Script

Use the local release script to validate everything before pushing:

```bash
# Run full release validation
python scripts/release.py 0.3.0

# Skip tests for faster validation
python scripts/release.py 0.3.0 --skip-tests

# Skip quality checks
python scripts/release.py 0.3.0 --skip-quality
```

The script will:
- Check git status
- Verify version consistency
- Validate changelog
- Run tests (unless skipped)
- Run quality checks (unless skipped)
- Build package
- Test installation
- Report success/failure

## Versioning

Follow [Semantic Versioning](https://semver.org/):

### Format
`MAJOR.MINOR.PATCH`

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality in backward compatible manner
- **PATCH**: Backward compatible bug fixes

### Examples
- `1.0.0` - First stable release
- `1.0.1` - Bug fix release
- `1.1.0` - Feature release
- `2.0.0` - Breaking changes release

### Prereleases
Add suffix for prereleases:
- `1.0.0-alpha.1`
- `1.0.0-beta.1`
- `1.0.0-rc.1`

## Release Checklist

### Before Release
- [ ] All tests pass locally
- [ ] Code quality checks pass
- [ ] Documentation is updated
- [ ] CHANGELOG.md is updated
- [ ] Version in pyproject.toml is correct
- [ ] Git working directory is clean

### During Release
- [ ] Tag is pushed (`vX.Y.Z`)
- [ ] GitHub Actions workflow starts
- [ ] Tests pass on all platforms
- [ ] Package builds successfully
- [ ] PyPI publishing succeeds
- [ ] GitHub release is created

### After Release
- [ ] Check PyPI listing
- [ ] Verify GitHub release
- [ ] Test installation from PyPI
- [ ] Update documentation if needed
- [ ] Announce release (optional)

## Troubleshooting

### Common Issues

#### 1. PyPI Publishing Fails
**Symptom**: Workflow fails at PyPI publish step
**Solution**:
- Check `PYPI_API_TOKEN` secret
- Verify token has publish permissions
- Ensure package name is not taken

#### 2. Tests Fail
**Symptom**: Tests fail during release workflow
**Solution**:
- Run tests locally: `poetry run pytest`
- Check platform-specific issues
- Fix failing tests before retrying

#### 3. Version Mismatch
**Symptom**: Workflow fails due to version inconsistency
**Solution**:
- Ensure tag version matches pyproject.toml
- Use `v` prefix in tags: `v0.3.0`
- Update CHANGELOG.md with correct version

#### 4. GitHub Release Creation Fails
**Symptom**: Release creation step fails
**Solution**:
- Check repository permissions
- Verify release notes format
- Ensure tag exists and is properly formatted

### Manual Recovery

If automated release fails, you can publish manually:

```bash
# Build package
poetry build

# Publish to PyPI
poetry publish

# Create GitHub release manually
# 1. Go to Releases page
# 2. Click "Create a new release"
# 3. Select tag
# 4. Add release notes
# 5. Upload build artifacts from dist/
```

## Post-Release Tasks

### 1. Verify Installation
```bash
# Test installation from PyPI
pip install pyside6-cutewindow

# Test import
python -c "import cutewindow; print('Success!')"
```

### 2. Update Documentation
- Update version in documentation
- Add release notes to website
- Update examples if needed

### 3. Announce Release
- Create GitHub discussion
- Post on social media (optional)
- Update project status (optional)

## Best Practices

1. **Test Thoroughly**: Always run the local release script before pushing tags
2. **Use Prereleases**: For major changes, use alpha/beta releases first
3. **Keep Changelog Updated**: Maintain detailed changelog for each release
4. **Monitor Releases**: Watch for any issues after release
5. **Document Breaking Changes**: Clearly document any breaking changes in changelog

## Security Considerations

- **PyPI Token**: Keep API token secure and limit permissions
- **Code Review**: Ensure all changes are reviewed before release
- **Dependency Scanning**: Run security checks before release
- **Access Control**: Limit release permissions to trusted maintainers

## Support

If you encounter issues during release:
1. Check workflow logs for detailed error messages
2. Review this guide for troubleshooting steps
3. Open an issue on GitHub with release-related problems
4. Contact maintainers for assistance
