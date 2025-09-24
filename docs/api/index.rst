API Reference
=============

This section contains the complete API reference for CuteWindow, with detailed documentation of all public classes and methods.

Core Classes
------------

CuteWindow
~~~~~~~~~

The main customizable window class that provides a modern, borderless window with native window controls.

**Constructor:**

.. code-block:: python

    CuteWindow(parent: Optional[QWidget] = None) -> None

**Key Methods:**

* ``titleBar() -> QWidget`` - Get the title bar widget
* ``setTitleBar(title_bar: QWidget) -> None`` - Set a custom title bar widget
* ``setNonResizable() -> None`` - Make the window non-resizable
* ``isResizable() -> bool`` - Check if the window is resizable

**Example:**

.. code-block:: python

    from cutewindow import QuteWindow

    window = QuteWindow()
    window.setWindowTitle("My App")
    window.resize(800, 600)
    window.show()

QuteMainWindow
~~~~~~~~~~~~~~

An advanced customizable window that supports menu bars and additional features typically found in main application windows.

**Constructor:**

.. code-block:: python

    QuteMainWindow(parent: Optional[QWidget] = None) -> None

**Key Methods:**

* ``titleBar() -> QWidget`` - Get the title bar widget
* ``setTitleBar(title_bar: QWidget) -> None`` - Set a custom title bar widget
* ``setNonResizable() -> None`` - Make the window non-resizable
* ``isResizable() -> bool`` - Check if the window is resizable
* ``setMenuBar(menubar: QMenuBar) -> None`` - Set the menu bar (inherited from QMainWindow)

**Example:**

.. code-block:: python

    from cutewindow import QuteMainWindow
    from PySide6.QtWidgets import QMenuBar, QMenu

    window = QuteMainWindow()
    window.setWindowTitle("Main App")

    # Add menu bar
    menubar = QMenuBar()
    file_menu = QMenu("File", menubar)
    menubar.addMenu(file_menu)
    window.setMenuBar(menubar)

    window.show()

QuteDialog
~~~~~~~~~~

A customizable dialog window with modal support, perfect for dialogs, forms, and popup windows.

**Constructor:**

.. code-block:: python

    QuteDialog(parent: Optional[QWidget] = None) -> None

**Key Methods:**

* ``titleBar() -> QWidget`` - Get the title bar widget
* ``setTitleBar(title_bar: QWidget) -> None`` - Set a custom title bar widget
* ``setNonResizable() -> None`` - Make the window non-resizable
* ``isResizable() -> bool`` - Check if the window is resizable
* ``setModal(modal: bool) -> None`` - Set dialog modality
* ``exec() -> int`` - Show dialog modally

**Example:**

.. code-block:: python

    from cutewindow import QuteDialog

    dialog = QuteDialog()
    dialog.setWindowTitle("Settings")
    dialog.setModal(True)
    dialog.exec()

TitleBar
~~~~~~~~

The default title bar widget that provides native window controls (close, minimize, maximize buttons).

**Constructor:**

.. code-block:: python

    TitleBar(parent: Optional[QWidget] = None) -> None

**Key Features:**

* Native window controls (close, minimize, maximize buttons)
* Platform-specific appearance and behavior
* Drag functionality for window movement
* Double-click to maximize/restore (Windows) or zoom (macOS)

Icon
~~~~

Enhanced QIcon class with automatic high-DPI support for better icon rendering on retina displays.

**Constructor:**

.. code-block:: python

    Icon(icon_path: Union[str, QPixmap, None] = None) -> None

**Key Methods:**

* ``addFile(fileName: str, size: Optional[QSize] = None, mode: Optional[QIcon.Mode] = None, state: Optional[QIcon.State] = None) -> None`` - Add an icon file with automatic high-DPI processing

**Key Features:**

* Automatic high-DPI icon loading
* Selects appropriate @2x.png files when needed
* Detects screen pixel ratio automatically

**Example:**

.. code-block:: python

    from cutewindow import Icon

    # Create icon with automatic high-DPI support
    icon = Icon("path/to/icon.png")
    window.setWindowIcon(icon)

Common Methods
--------------

All QuteWindow classes inherit from QWidget and provide these common methods:

Window Management
~~~~~~~~~~~~~~~~~

* ``setWindowTitle(title: str) -> None`` - Set the window title
* ``setWindowIcon(icon: QIcon) -> None`` - Set the window icon
* ``resize(width: int, height: int) -> None`` - Resize the window
* ``show() -> None`` - Show the window
* ``hide() -> None`` - Hide the window
* ``close() -> None`` - Close the window

Title Bar Customization
~~~~~~~~~~~~~~~~~~~~~~~~

* ``titleBar() -> QWidget`` - Get the current title bar widget
* ``setTitleBar(title_bar: QWidget) -> None`` - Set a custom title bar widget

Resizability Control
~~~~~~~~~~~~~~~~~~~~

* ``setNonResizable() -> None`` - Make the window non-resizable
* ``isResizable() -> bool`` - Check if the window is resizable

Platform Factory Functions
--------------------------

For advanced usage, you can access platform factory functions:

* ``get_platform_name() -> str`` - Get the current platform name ("mac", "windows", or "linux")
* ``get_qute_window_class() -> Type[BaseQuteWindow]`` - Get the appropriate QuteWindow class for the current platform
* ``get_qute_main_window_class() -> Type[BaseQuteWindow]`` - Get the appropriate QuteMainWindow class for the current platform
* ``get_qute_dialog_class() -> Type[BaseQuteWindow]`` - Get the appropriate QuteDialog class for the current platform
* ``get_title_bar_class() -> Type[BaseTitleBar]`` - Get the appropriate TitleBar class for the current platform

Base Classes (For Advanced Users)
---------------------------------

These abstract base classes define the interface that all platform-specific implementations must follow:

**BaseQuteWindow**
  Abstract base class for all QuteWindow implementations

**BaseTitleBar**
  Abstract base class for all TitleBar implementations

Platform-Specific Details
~~~~~~~~~~~~~~~~~~~~~~~~

The following modules contain platform-specific implementations. You typically don't need to use these directly, but they're documented here for reference and advanced customization.

**macOS Implementation**
  * Native traffic light buttons (red, yellow, green)
  * Smooth window animations
  * Full-screen support
  * Mission Control integration

**Windows Implementation**
  * Native window shadows via DWM
  * Windows 11 snap layout support
  * Smooth window animations
  * Native window buttons
  * Aero Snap functionality

Utility Modules
---------------

Platform-specific utility functions used internally:

**macOS Utilities**
  * ``merge_content_area_and_title_bar()`` - Merge content area and title bar on macOS
  * ``setTrafficLightsPosition()`` - Set position of traffic light buttons
  * ``setWindowNonResizable()`` - Make window non-resizable on macOS
  * ``startSystemMove()`` - Start system window movement on macOS

**Windows Utilities**
  * ``addShadowEffect()`` - Add DWM shadow effect to window
  * ``addWindowAnimation()`` - Add window animations on Windows
  * ``setWindowNonResizable()`` - Make window non-resizable on Windows
  * ``isMaximized()`` - Check if window is maximized
  * ``isFullScreen()`` - Check if window is in fullscreen mode
  * ``startSystemMove()`` - Start system window movement on Windows

**Windows Native Event Handling**
  * Low-level Windows message processing
  * Hit testing for window resizing
  * Custom window button handling

**Windows C Structures**
  * Low-level Windows API structures
  * Used for native window operations
