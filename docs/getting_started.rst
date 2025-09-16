Getting Started
===============

QuteWindow is a modern, cross-platform frameless window library for Python and Qt that provides native window controls and behaviors across different platforms.

Installation
------------

From PyPI
~~~~~~~~~

Install QuteWindow with a single command::

    pip install qutewindow

From Source
~~~~~~~~~~~

.. code-block:: bash

    git clone https://github.com/parhamoyan/qutewindow.git
    cd qutewindow
    pip install -e .

Basic Usage
-----------

Creating a frameless window is as simple as:

.. code-block:: python

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

Window Types
------------

QuteWindow provides three main window types for different use cases.

QuteWindow (Basic)
~~~~~~~~~~~~~~~~~~

The basic frameless window with native window controls.

.. code-block:: python

    from qutewindow import QuteWindow

    window = QuteWindow()
    window.setWindowTitle("Basic Window")
    window.show()

QuteMainWindow (Advanced)
~~~~~~~~~~~~~~~~~~~~~~~~~

Advanced window with menu bar support and additional features.

.. code-block:: python

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

QuteDialog (Dialogs)
~~~~~~~~~~~~~~~~~~~~

Frameless dialog windows with modal support.

.. code-block:: python

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

Next Steps
----------

* :doc:`api/index` - Complete API reference
* :doc:`examples/index` - Usage examples
* :doc:`customization` - Customization guide