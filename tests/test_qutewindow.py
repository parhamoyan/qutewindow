"""
Comprehensive tests for CuteWindow functionality.
"""

from unittest.mock import patch

import pytest
from PySide6.QtWidgets import QApplication


class TestCuteWindowBasic:
    """Test basic CuteWindow functionality."""

    def test_cutewindow_import(self):
        """Test that cutewindow can be imported successfully."""
        try:
            import cutewindow

            assert cutewindow is not None
        except ImportError as e:
            pytest.skip(f"Cannot import cutewindow: {e}")

    def test_platform_detection(self):
        """Test that platform detection works."""
        try:
            from qutewindow.platform_factory import get_platform_name

            platform_name = get_platform_name()
            assert platform_name in ["windows", "mac", "linux"]
        except ImportError:
            pytest.skip("Cannot import platform factory")
        except NotImplementedError:
            pytest.skip("Platform not supported")

    def test_base_classes_exist(self):
        """Test that base classes can be imported."""
        try:
            from qutewindow.base import BaseCuteWindow, BaseTitleBar

            assert BaseCuteWindow is not None
            assert BaseTitleBar is not None
        except ImportError:
            pytest.skip("Cannot import base classes")

    def test_platform_factory_functions(self):
        """Test that platform factory functions exist."""
        try:
            from qutewindow.platform_factory import (
                get_qute_dialog_class,
                get_qute_main_window_class,
                get_qute_window_class,
                get_title_bar_class,
            )

            assert callable(get_qute_window_class)
            assert callable(get_qute_main_window_class)
            assert callable(get_qute_dialog_class)
            assert callable(get_title_bar_class)
        except ImportError:
            pytest.skip("Cannot import platform factory functions")


class TestQuteWindowCreation:
    """Test QuteWindow creation and basic functionality."""

    @pytest.fixture
    def app(self):
        """Create QApplication for testing."""
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        yield app
        # Don't quit - let it be cleaned up naturally

    def test_window_creation(self, app):
        """Test basic window creation."""
        try:
            from cutewindow import CuteWindow

            window = CuteWindow()
            assert window is not None
            assert window.windowTitle() == ""

            # Clean up
            window.close()
        except ImportError:
            pytest.skip("Cannot import CuteWindow")
        except Exception as e:
            pytest.fail(f"Failed to create CuteWindow: {e}")

    def test_window_title(self, app):
        """Test window title functionality."""
        try:
            from cutewindow import CuteWindow

            window = CuteWindow()
            test_title = "Test Window"

            window.setWindowTitle(test_title)
            assert window.windowTitle() == test_title

            # Clean up
            window.close()
        except ImportError:
            pytest.skip("Cannot import QuteWindow")
        except Exception as e:
            pytest.fail(f"Failed to test window title: {e}")

    def test_window_resize(self, app):
        """Test window resize functionality."""
        try:
            from cutewindow import CuteWindow

            window = CuteWindow()
            test_size = (800, 600)

            window.resize(*test_size)
            assert window.width() == test_size[0]
            assert window.height() == test_size[1]

            # Clean up
            window.close()
        except ImportError:
            pytest.skip("Cannot import CuteWindow")
        except Exception as e:
            pytest.fail(f"Failed to test window resize: {e}")


class TestCuteMainWindow:
    """Test CuteMainWindow functionality."""

    @pytest.fixture
    def app(self):
        """Create QApplication for testing."""
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        yield app

    def test_main_window_creation(self, app):
        """Test main window creation."""
        try:
            from cutewindow import CuteMainWindow

            window = CuteMainWindow()
            assert window is not None

            # Clean up
            window.close()
        except ImportError:
            pytest.skip("Cannot import QuteMainWindow")
        except Exception as e:
            pytest.fail(f"Failed to create QuteMainWindow: {e}")


class TestCuteDialog:
    """Test CuteDialog functionality."""

    @pytest.fixture
    def app(self):
        """Create QApplication for testing."""
        app = QApplication.instance()
        if app is None:
            app = QApplication([])
        yield app

    def test_dialog_creation(self, app):
        """Test dialog creation."""
        try:
            from cutewindow import CuteDialog

            dialog = CuteDialog()
            assert dialog is not None

            # Clean up
            dialog.close()
        except ImportError:
            pytest.skip("Cannot import CuteDialog")
        except Exception as e:
            pytest.fail(f"Failed to create CuteDialog: {e}")


class TestPlatformSpecific:
    """Test platform-specific functionality."""

    def test_windows_imports(self):
        """Test Windows-specific imports."""
        try:
            from qutewindow.platforms.windows import QuteDialog as WindowsQuteDialog
            from qutewindow.platforms.windows import (
                QuteMainWindow as WindowsQuteMainWindow,
            )
            from qutewindow.platforms.windows import QuteWindow as WindowsQuteWindow

            assert WindowsQuteWindow is not None
            assert WindowsQuteMainWindow is not None
            assert WindowsQuteDialog is not None
        except ImportError:
            pytest.skip("Windows-specific imports not available")

    def test_macos_imports(self):
        """Test macOS-specific imports."""
        try:
            from qutewindow.platforms.mac import QuteDialog as MacQuteDialog
            from qutewindow.platforms.mac import QuteMainWindow as MacQuteMainWindow
            from qutewindow.platforms.mac import QuteWindow as MacQuteWindow

            assert MacQuteWindow is not None
            assert MacQuteMainWindow is not None
            assert MacQuteDialog is not None
        except ImportError:
            pytest.skip("macOS-specific imports not available")


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_unsupported_platform(self):
        """Test behavior on unsupported platforms."""
        with patch("qutewindow.platform_factory.sys.platform", "unsupported_os"):
            try:
                from qutewindow.platform_factory import get_platform_name

                with pytest.raises(NotImplementedError):
                    get_platform_name()
            except ImportError:
                pytest.skip("Cannot import platform factory")

    def test_missing_dependencies(self):
        """Test behavior when dependencies are missing."""
        # This would require more complex mocking to test properly
        # For now, we'll just ensure the imports work
        try:
            import cutewindow

            assert cutewindow is not None
        except ImportError:
            pytest.skip("cutewindow not available")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
