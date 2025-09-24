Customization
=============

CuteWindow provides several ways to customize the appearance and behavior of your customizable windows.

Styling the Title Bar
---------------------

You can style the title bar using CSS stylesheets:

.. code-block:: python

    from cutewindow import CuteWindow

    window = CuteWindow()

    # Style the title bar using CSS
    window.setStyleSheet("""
        #TitleBar {
            background-color: #2b2b2b;
            border-bottom: 1px solid #3a3a3a;
        }
        #TitleBar QLabel {
            color: white;
            font-weight: bold;
        }
    """)

    window.show()

Custom Title Bar Widget
-----------------------

You can create a completely custom title bar by subclassing the TitleBar class:

.. code-block:: python

    from PySide6.QtWidgets import QLabel, QPushButton, QHBoxLayout, QWidget
    from cutewindow import CuteWindow, TitleBar

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
            help_btn.clicked.connect(self.show_help)
            layout.addWidget(help_btn)

        def show_help(self):
            print("Help clicked!")

    window = CuteWindow()
    window.setTitleBar(CustomTitleBar(window))
    window.show()

Window Resizability
-------------------

Control whether the window can be resized:

.. code-block:: python

    from cutewindow import CuteWindow

    window = CuteWindow()

    # Make window non-resizable
    window.setNonResizable()

    # Check if window is resizable
    if window.isResizable():
        print("Window is resizable")
    else:
        print("Window is not resizable")

    window.show()

Platform-Specific Customization
--------------------------------

Windows Customization
~~~~~~~~~~~~~~~~~~~~~

On Windows, you can access additional Windows-specific features:

.. code-block:: python

    from cutewindow import CuteWindow

    window = CuteWindow()

    # Windows-specific styling
    if sys.platform == 'win32':
        window.setStyleSheet("""
            #TitleBar {
                background-color: #0078d4;
                border-bottom: 1px solid #005a9e;
            }
        """)

    window.show()

macOS Customization
~~~~~~~~~~~~~~~~~~~

On macOS, you can customize the traffic light buttons:

.. code-block:: python

    from cutewindow import CuteWindow

    window = CuteWindow()

    # macOS-specific styling
    if sys.platform == 'darwin':
        window.setStyleSheet("""
            #TitleBar {
                background-color: #f0f0f0;
                border-bottom: 1px solid #d1d1d1;
            }
        """)

    window.show()

Icon Customization
------------------

Set custom window icons:

.. code-block:: python

    from PySide6.QtGui import QIcon
    from cutewindow import CuteWindow, Icon

    window = CuteWindow()

    # Set window icon
    icon = QIcon("path/to/icon.png")
    window.setWindowIcon(icon)

    # Use enhanced Icon class for better icon handling
    enhanced_icon = Icon("path/to/icon.png")
    window.setWindowIcon(enhanced_icon)

    window.show()
