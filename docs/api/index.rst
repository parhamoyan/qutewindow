API Reference
=============

This section contains the complete API reference for QuteWindow, automatically generated from the source code docstrings.

The API is organized into several sections:

**Core Public API**
  The main classes and functions you'll use as a developer

**Platform Factory** 
  Factory functions for creating platform-specific components

**Base Classes**
  Abstract base classes that define the common interface

**Platform-Specific Implementations**
  Detailed documentation for each platform's internal implementation

**Utility Modules**
  Helper functions and platform-specific utilities

Core Public API
---------------

These are the main classes and functions you'll use in your applications.

.. automodule:: qutewindow
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.Icon
   :members:
   :undoc-members:
   :show-inheritance:

Platform Factory
----------------

Factory functions for creating platform-specific components. These are used internally but can be useful for advanced use cases.

.. automodule:: qutewindow.platform_factory
   :members:
   :undoc-members:
   :show-inheritance:

Base Classes
------------

Abstract base classes that define the common interface for all platform-specific implementations.

.. automodule:: qutewindow.base
   :members:
   :undoc-members:
   :show-inheritance:

Platform-Specific Implementations
---------------------------------

These modules contain the platform-specific implementations. You typically don't need to use these directly, but they're documented here for reference and advanced customization.

macOS Platform
~~~~~~~~~~~~~~

.. automodule:: qutewindow.platforms.mac
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.mac.QuteWindow
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.mac.QuteMainWindow
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.mac.QuteDialog
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.mac.title_bar.TitleBar
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.mac.utils
   :members:
   :undoc-members:
   :show-inheritance:

Windows Platform
~~~~~~~~~~~~~~~~

.. automodule:: qutewindow.platforms.windows
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.QuteWindow
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.QuteMainWindow
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.QuteDialog
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.title_bar.TitleBar
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.utils
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.native_event
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: qutewindow.platforms.windows.c_structures
   :members:
   :undoc-members:
   :show-inheritance: