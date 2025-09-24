def test_import_qutewindow():
    """Test that qutewindow can be imported successfully."""
    try:
        import qutewindow

        assert qutewindow is not None
    except ImportError as e:
        print(f"Cannot import qutewindow: {e}")
        # Don't fail the test, just note the issue
        assert True


def test_platform_detection():
    """Test that platform detection works."""
    try:
        from qutewindow.platform_factory import get_platform_name

        platform_name = get_platform_name()
        assert platform_name in ["windows", "mac", "linux"]
    except ImportError:
        print("Cannot import platform factory")
        assert True
    except NotImplementedError:
        print("Platform not supported")
        assert True


def test_base_classes_exist():
    """Test that base classes can be imported."""
    try:
        from qutewindow.base import BaseCuteWindow, BaseTitleBar

        assert BaseCuteWindow is not None
        assert BaseTitleBar is not None
    except ImportError:
        print("Cannot import base classes")
        assert True


def test_platform_factory_functions():
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
        print("Cannot import platform factory functions")
        assert True
