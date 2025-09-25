"""Basic tests for CuteWindow package."""


def test_import():
    """Test that the package can be imported."""
    try:
        import cutewindow

        assert cutewindow is not None
        print("✅ CuteWindow imported successfully")
    except ImportError as e:
        assert False, f"Failed to import cutewindow: {e}"


def test_base_import():
    """Test that base classes can be imported."""
    try:
        from cutewindow.base import BaseCuteWindow

        assert BaseCuteWindow is not None
        print("✅ BaseCuteWindow imported successfully")
    except ImportError as e:
        assert False, f"Failed to import BaseCuteWindow: {e}"


def test_platform_factory_import():
    """Test that platform factory functions can be imported."""
    try:
        from cutewindow.platform_factory import get_cute_window_class, get_platform_name

        assert get_platform_name is not None
        assert get_cute_window_class is not None
        print("✅ Platform factory functions imported successfully")
    except ImportError as e:
        assert False, f"Failed to import platform factory functions: {e}"
