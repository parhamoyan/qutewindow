"""
Pytest configuration and shared fixtures for QuteWindow tests.
"""

import sys
from typing import Generator

import pytest
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def app() -> Generator[QCoreApplication, None, None]:
    """
    Create and return a QApplication instance for testing.

    This fixture is session-scoped to avoid creating multiple QApplication instances,
    which can cause issues with Qt.

    Yields:
        QCoreApplication: The Qt application instance
    """
    application = QApplication.instance()
    if application is None:
        application = QApplication(sys.argv)

    yield application

    # Don't quit the app - let it be cleaned up naturally


@pytest.fixture
def qapp(app: QCoreApplication) -> QCoreApplication:
    """
    Fixture that provides the QApplication instance.

    This is an alias for the 'app' fixture for convenience.
    """
    return app


@pytest.fixture(autouse=True)
def cleanup_qt_objects():
    """
    Automatically clean up Qt objects after each test.

    This helps prevent memory leaks and ensures that Qt objects
    are properly cleaned up between tests.
    """
    yield
    # Qt objects will be cleaned up automatically when they go out of scope
