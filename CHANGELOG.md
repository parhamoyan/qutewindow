# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2024-09-25

### Fixed
- Updated release workflow to use Trusted Publishing instead of API tokens
- Fixed missing dev dependencies in pyproject.toml
- Added basic test structure for release validation

## [0.1.0] - 2024-09-24

### Added
- Cross-platform customizable window support
- Windows-specific implementation with native controls
- macOS-specific implementation with native traffic lights
- Custom title bar functionality
- High-DPI support
- Native window animations
- Windows 11 snap layout support
- Updated package description and terminology from frameless to customizable

### Changed
- Modular architecture with platform-specific implementations
- Improved API design
- Enhanced documentation with consistent terminology

### Added
- Cross-platform customizable window support
- Windows-specific implementation with native controls
- macOS-specific implementation with native traffic lights
- Custom title bar functionality
- High-DPI support
- Native window animations
- Windows 11 snap layout support

### Changed
- Modular architecture with platform-specific implementations
- Improved API design

## [0.1.0] - 2024-09-24 (Planned)

### Added
- Initial project structure
- Basic window functionality
- Platform detection system
- Documentation setup
- CI/CD pipeline

---

## Release Process

### Automated Releases

This project uses automated releases through GitHub Actions. When you push a tag matching the pattern `v*` (e.g., `v0.3.0`, `v1.0.0`), the following happens automatically:

1. **Tests**: Run comprehensive tests across multiple Python versions and platforms
2. **Build**: Build the package using Poetry
3. **Publish**: Publish to PyPI using trusted publishing
4. **Release**: Create a GitHub Release with changelog and build artifacts

### Manual Releases

You can also trigger a manual release through the GitHub Actions UI:

1. Go to the Actions tab in your repository
2. Select the "Release" workflow
3. Click "Run workflow"
4. Fill in the version and prerelease information
5. Click "Run workflow"

### Prerequisites

Before creating a release, ensure:

1. **Update CHANGELOG.md**: Add a new section for the upcoming release with all changes
2. **Update version in pyproject.toml**: The version should match the tag you're creating
3. **All tests pass**: Run `poetry run pytest` locally
4. **Code quality checks pass**: Run `poetry run python scripts/quality_check.py`

### Versioning

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **MAJOR**: Incompatible changes
- **MINOR**: New functionality in a backward compatible manner
- **PATCH**: Backward compatible bug fixes

### Tag Format

Use the following tag format: `v{major}.{minor}.{patch}`

Examples:
- `v1.0.0` - First stable release
- `v1.0.1` - Patch release
- `v1.1.0` - Minor release with new features
- `v2.0.0` - Major release with breaking changes

### Prereleases

For prereleases, append a suffix:

- `v1.0.0-alpha.1`
- `v1.0.0-beta.1`
- `v1.0.0-rc.1`

These will be marked as prereleases on GitHub and PyPI.

---

## Types of Changes

- `Added` for new features
- `Changed` for changes in existing functionality
- `Deprecated` for soon-to-be removed features
- `Removed` for now removed features
- `Fixed` for any bug fixes
- `Security` in case of vulnerabilities
