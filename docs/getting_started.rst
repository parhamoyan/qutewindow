Getting Started
===============

CuteWindow is a modern, cross-platform window library for Python and Qt that provides enhanced control and customization with native window controls and behaviors across different platforms.

Installation
------------

From PyPI
~~~~~~~~~

Install CuteWindow with a single command::

    pip install pyside6-cutewindow

From Source
~~~~~~~~~~~

.. code-block:: bash

    git clone https://github.com/parhamoyan/cutewindow.git
    cd cutewindow
    pip install -e .

Basic Usage
-----------

Creating a customizable window is as simple as:

.. code-block:: python

    import sys
    from PySide6.QtWidgets import QApplication
    from cutewindow import CuteWindow

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = CuteWindow()
        window.setWindowTitle("My Customizable App")
        window.resize(800, 600)
        window.show()
        sys.exit(app.exec())

Window Types
------------

CuteWindow provides three main window types for different use cases.

CuteWindow (Basic)
~~~~~~~~~~~~~~~~~~

The basic customizable window with native window controls.

.. code-block:: python

    from cutewindow import CuteWindow

    window = CuteWindow()
    window.setWindowTitle("Basic Window")
    window.show()

QuteMainWindow (Advanced)
~~~~~~~~~~~~~~~~~~~~~~~~~

Advanced window with menu bar support and additional features.

.. code-block:: python

    from cutewindow import QuteMainWindow
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

QuteDialog (Dialogs)
~~~~~~~~~~~~~~~~~~~~

Customizable dialog windows with modal support.

.. code-block:: python

    from cutewindow import QuteDialog
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

Next Steps
----------

* :doc:`api/index` - Complete API reference
* :doc:`examples/index` - Usage examples
* :doc:`customization` - Customization guide
