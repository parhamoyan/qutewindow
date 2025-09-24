# QuteWindow

[![PyPI version](https://badge.fury.io/py/qutewindow.svg)](https://badge.fury.io/py/qutewindow)
[![Python Support](https://img.shields.io/pypi/pyversions/qutewindow.svg)](https://pypi.org/project/qutewindow/)
[![License](https://img.shields.io/github/license/parhamoyan/qutewindow.svg)](https://github.com/parhamoyan/qutewindow/blob/main/LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/parhamoyan/qutewindow/workflows/CI/badge.svg)](https://github.com/parhamoyan/qutewindow/actions/workflows/ci.yml)
[![Documentation](https://github.com/parhamoyan/qutewindow/workflows/Documentation/badge.svg)](https://github.com/parhamoyan/qutewindow/actions/workflows/docs.yml)

**QuteWindow** is a modern, cross-platform frameless window library for Python and Qt that provides native window controls and behaviors across different platforms. Create beautiful, frameless applications with ease!

## ✨ Features

- 🖥️ **Cross-platform**: Works seamlessly on Windows and macOS
- 🎨 **Frameless design**: Clean, modern window appearance without system chrome
- 🎛️ **Native controls**: Platform-specific window buttons and behaviors
- 🎯 **Customizable**: Easy to customize title bar appearance and functionality
- 📱 **High-DPI support**: Automatic scaling for high-resolution displays
- ✨ **Native animations**: Smooth window animations and shadows
- 🪟 **Win11 snap layout**: Windows 11 snap layout support
- 🔧 **Easy integration**: Drop-in replacement for standard Qt windows

## 🚀 Quick Start

### Installation

Install QuteWindow with a single command:

```bash
pip install qutewindow
```

### Basic Usage

Creating a frameless window is as simple as:

```python
import sys
from PySide6.QtWidgets import QApplication
from qutewindow import QuteWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuteWindow()
    window.setWindowTitle("My Frameless App")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
```

### Window Types

QuteWindow provides three main window types for different use cases:

#### QuteWindow (Basic)
```python
from qutewindow import QuteWindow

window = QuteWindow()
window.setWindowTitle("Basic Window")
window.show()
```

#### QuteMainWindow (Advanced)
```python
from qutewindow import QuteMainWindow
from PySide6.QtWidgets import QMenuBar, QMenu, QAction

window = QuteMainWindow()
window.setWindowTitle("Main Window")

# Add menu bar
menubar = QMenuBar()
file_menu = QMenu("File", menubar)
exit_action = QAction("Exit", menubar)
file_menu.addAction(exit_action)
menubar.addMenu(file_menu)
window.setMenuBar(menubar)

window.show()
```

#### QuteDialog (Dialogs)
```python
from qutewindow import QuteDialog
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget

dialog = QuteDialog()
dialog.setWindowTitle("Dialog")
dialog.setModal(True)

# Add content
layout = QVBoxLayout()
button = QPushButton("Close")
button.clicked.connect(dialog.close)
layout.addWidget(button)

container = QWidget()
container.setLayout(layout)
dialog.setCentralWidget(container)

dialog.exec()
```

## 🎨 Customization

### Styling the Title Bar

```python
from qutewindow import QuteWindow

window = QuteWindow()

# Style the title bar using CSS
window.setStyleSheet("""
    #TitleBar {
        background-color: #2b2b2b;
        border-bottom: 1px solid #3a3a3a;
    }
""")

window.show()
```

### Custom Title Bar Widget

```python
from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget
from qutewindow import QuteWindow, TitleBar

class CustomTitleBar(TitleBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Create custom layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 10, 0)

        # Add title label
        title_label = QLabel("Custom Title")
        title_label.setStyleSheet("color: white; font-weight: bold;")
        layout.addWidget(title_label)

        layout.addStretch()

        # Add custom buttons
        help_btn = QPushButton("?")
        help_btn.setFixedSize(30, 20)
        layout.addWidget(help_btn)

window = QuteWindow()
window.setTitleBar(CustomTitleBar(window))
window.show()
```

## 🖼️ Screenshots

### QuteWindow on macOS
<p align="center">
  <img src="readme/mac_qute_window.gif" alt="QuteWindow on macOS" width="600">
</p>

### QuteWindow on Windows
<p align="center">
  <img src="readme/win32_qute_window.gif" alt="QuteWindow on Windows" width="600">
</p>

## 📋 Requirements

- **Python**: 3.9 or higher
- **Poetry**: Dependency management (recommended)
- **PySide6**: Qt6 bindings for Python
- **Platform-specific dependencies**:
  - **macOS**: pyobjc-framework-Cocoa, pyobjc-framework-Quartz
  - **Windows**: pywin32

## 🔧 Installation

### From PyPI (Recommended)

```bash
pip install qutewindow
```

### From Source with Poetry (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/parhamoyan/qutewindow.git
cd qutewindow

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies
poetry install

# Set up development environment
poetry install --with dev

# Set up pre-commit hooks
poetry run python scripts/setup_precommit.py
```

### From Source with pip

```bash
git clone https://github.com/parhamoyan/qutewindow.git
cd qutewindow
pip install -e .
```

### Development Installation with pip

```bash
git clone https://github.com/parhamoyan/qutewindow.git
cd qutewindow
pip install -e ".[dev]"
pre-commit install
```

## 📚 Documentation

Comprehensive documentation is available at [https://qutewindow.readthedocs.io](https://qutewindow.readthedocs.io)

- [Installation Guide](https://qutewindow.readthedocs.io/en/latest/installation.html)
- [Quick Start Guide](https://qutewindow.readthedocs.io/en/latest/quickstart.html)
- [API Reference](https://qutewindow.readthedocs.io/en/latest/api/index.html)
- [Examples](https://qutewindow.readthedocs.io/en/latest/examples/index.html)

## 🎯 Examples

Check out the `examples/` directory for more comprehensive examples:

- `demo.py` - Basic usage example
- `demo_custom_title_bar.py` - Custom title bar implementation
- `demo_login_dialog.py` - Login dialog example
- `demo_title_bar_style.py` - Title bar styling example

Run an example:

```bash
python examples/demo.py
```

## 🏗️ Architecture

QuteWindow uses a clean, modular architecture:

```
qutewindow/
├── __init__.py                 # Main package interface
├── base.py                     # Abstract base classes
├── Icon.py                     # Enhanced icon handling
├── platforms/                  # Platform-specific implementations
│   ├── __init__.py            # Platform detection
│   ├── mac/                   # macOS implementation
│   │   ├── QuteWindow.py
│   │   ├── QuteMainWindow.py
│   │   ├── QuteDialog.py
│   │   ├── TitleBar.py
│   │   └── utils.py
│   └── windows/               # Windows implementation
│       ├── QuteWindow.py
│       ├── QuteMainWindow.py
│       ├── QuteDialog.py
│       ├── TitleBar.py
│       ├── utils.py
│       ├── native_event.py
│       └── c_structures.py
└── examples/                   # Usage examples
```

### Platform-Specific Features

#### Windows
- Native window shadows via DWM
- Windows 11 snap layout support
- Smooth window animations
- Native window buttons
- Aero Snap functionality

#### macOS
- Native traffic lights (red, yellow, green buttons)
- Smooth window animations
- Full-screen support
- Native window shadows
- Mission Control integration

## 🔄 CI/CD

QuteWindow uses GitHub Actions for continuous integration and deployment:

- **CI Pipeline**: Runs on every push and pull request to ensure code quality
  - Tests across multiple Python versions (3.8-3.12) and platforms (Windows, macOS, Linux)
  - Code formatting checks (Black, isort)
  - Linting (flake8)
  - Type checking (mypy)
  - Security scanning (safety, bandit)
  - Package building and installation testing

- **Documentation**: Automatically builds and deploys documentation to GitHub Pages
- **Code Coverage**: Tracks test coverage with Codecov integration
- **Automated Publishing**: Publishes to PyPI when new tags are created

### Quality Checks

The CI pipeline enforces the following quality standards:

- **Code Style**: Black formatting and isort import sorting
- **Type Safety**: Mypy static type checking
- **Code Quality**: Flake8 linting with strict rules
- **Security**: Dependency and code security scanning
- **Testing**: Comprehensive test suite with coverage reporting

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/qutewindow.git`
3. Navigate to the project: `cd qutewindow`
4. Install dependencies with Poetry: `poetry install --with dev`
5. Set up pre-commit hooks: `poetry run python scripts/setup_precommit.py`
6. Create your feature branch: `git checkout -b feature/amazing-feature`
7. Make your changes and ensure they pass tests: `poetry run pytest`
8. Run quality checks: `poetry run python scripts/quality_check.py`
9. Format your code: `poetry run python scripts/format_code.py` or `poetry run black . && poetry run isort .`
10. Commit your changes: `git commit -m 'feat: add amazing feature'`
11. Push to the branch: `git push origin feature/amazing-feature`
12. Open a Pull Request

### Code Style

We use:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking
- **bandit** for security scanning
- **safety** for dependency safety

### Development Tools

The project includes several convenience scripts:

```bash
# Run comprehensive quality checks
poetry run python scripts/quality_check.py

# Run all tests
poetry run python scripts/run_tests.py

# Auto-format code
poetry run python scripts/format_code.py

# Set up pre-commit hooks
poetry run python scripts/setup_precommit.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Support

- 📧 **Email**: parhamoyan@yahoo.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/parhamoyan/qutewindow/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/parhamoyan/qutewindow/discussions)
- 📖 **Documentation**: [Read the Docs](https://qutewindow.readthedocs.io)

## 🗺️ Roadmap

- [ ] Additional window customization options
- [ ] More examples and tutorials
- [ ] PyQt6 support

---

**Made with ❤️ by Parham Oyan**
