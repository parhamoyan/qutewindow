"""
Windows-specific TitleBar implementation.

This module provides the Windows-specific implementation of the TitleBar class,
which creates a native-looking title bar for customizable windows on Windows.
Unlike the macOS version, the Windows title bar includes custom window controls
(close, minimize, maximize) that match the Windows visual style.
"""

from enum import Enum, IntEnum, auto
from typing import Optional

from PySide6.QtCore import QEvent, QSize
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QWidget,
)

# Never remove the following resources_rc import, it is used to load title bar icons
import cutewindow.platforms.windows.title_bar.resources_rc
from cutewindow.Icon import Icon
from cutewindow.platforms.windows.utils import startSystemMove


class MaximizeButtonIcon(str, Enum):
    """
    Enumeration of maximize button icon types.

    This enum defines the two possible states for the maximize button icon:
    - RESTORE: Show the restore icon (when window is maximized)
    - MAXIMIZE: Show the maximize icon (when window is normal size)
    """

    RESTORE = "restore"
    MAXIMIZE = "maximize"


class TitleBarButton(QPushButton):
    """
    Base class for title bar buttons.

    This class provides common styling and behavior for all title bar buttons.
    It sets a fixed size and icon size to ensure consistent appearance across
    all window control buttons.

    Attributes:
        None (inherits from QPushButton)

    Example:
        >>> button = TitleBarButton(parent=title_bar)
        >>> button.setIcon(Icon(":/icons/title-bar/close.png"))
    """

    def __init__(self, parent: Optional[QWidget]) -> None:
        """
        Initialize the title bar button.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(TitleBarButton, self).__init__(parent)

        # Set fixed size for consistent button appearance
        self.setFixedSize(QSize(40, 28))

        # Set icon size to fit within the button
        self.setIconSize(QSize(24, 24))


class MaximizeButtonState(IntEnum):
    """
    Enumeration of maximize button visual states.

    This enum defines the visual states for the maximize button:
    - HOVER: Button is being hovered by the mouse
    - NORMAL: Button is in normal (non-hovered) state
    """

    HOVER = auto()
    NORMAL = auto()


class MaximizeButton(TitleBarButton):
    """
    Maximize/Restore button for the title bar.

    This button handles window maximization and restoration. It changes its
    icon based on the current window state and provides visual feedback
    on hover.

    Features:
    - Changes icon between maximize and restore based on window state
    - Provides hover effects with background color changes
    - Maintains consistent styling with other title bar buttons

    Attributes:
        None (inherits from TitleBarButton)

    Example:
        >>> maximize_btn = MaximizeButton(parent=title_bar)
        >>> maximize_btn.clicked.connect(window.showMaximized)
    """

    def __init__(self, parent: Optional[QWidget]) -> None:
        """
        Initialize the maximize button.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(MaximizeButton, self).__init__(parent)

        # Set default styling for the button
        self.setStyleSheet(
            """
        QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton::hover {
        	background-color: #1D1D24;
        }
        """
        )

        # Set initial maximize icon
        self.setIcon(Icon(":/icons/title-bar/maximize.png"))

    def setState(self, state: MaximizeButtonState) -> None:
        """
        Set the visual state of the maximize button.

        This method changes the button's styling based on its state,
        primarily to provide hover effects.

        Args:
            state (MaximizeButtonState): The visual state to set.
        """
        if state == MaximizeButtonState.HOVER:
            # Apply hover styling with dark background
            self.setStyleSheet(
                """
                    QPushButton {
                        background-position: center;
                        background-repeat: no-repeat;
                        border: none;
                        outline: none;
                        color: #d1d3d2;
                        background-color: #1D1D24;
                    }
                    """
            )
        elif state == MaximizeButtonState.NORMAL:
            # Apply normal styling with transparent background
            self.setStyleSheet(
                """
                    QPushButton {
                        background-position: center;
                        background-repeat: no-repeat;
                        border: none;
                        outline: none;
                        color: #d1d3d2;
                        background: transparent;
                    }
                    """
            )
        self.update()


class MinimizeButton(TitleBarButton):
    """
    Minimize button for the title bar.

    This button handles window minimization. It provides a consistent
    appearance with other title bar buttons and hover effects.

    Features:
    - Minimizes the window when clicked
    - Provides hover effects with background color changes
    - Maintains consistent styling with other title bar buttons

    Attributes:
        None (inherits from TitleBarButton)

    Example:
        >>> minimize_btn = MinimizeButton(parent=title_bar)
        >>> minimize_btn.clicked.connect(window.showMinimized)
    """

    def __init__(self, parent: Optional[QWidget]) -> None:
        """
        Initialize the minimize button.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(MinimizeButton, self).__init__(parent)

        # Set styling for the minimize button
        self.setStyleSheet(
            """
                QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton::hover {
        	background-color: #1D1D24;
        }
        """
        )

        # Set minimize icon
        self.setIcon(Icon(":/icons/title-bar/minimize.png"))


class CloseButton(TitleBarButton):
    """
    Close button for the title bar.

    This button handles window closing. It provides a distinctive red
    hover effect to match Windows UI conventions and consistent
    appearance with other title bar buttons.

    Features:
    - Closes the window when clicked
    - Provides red hover effect (Windows convention)
    - Maintains consistent styling with other title bar buttons

    Attributes:
        None (inherits from TitleBarButton)

    Example:
        >>> close_btn = CloseButton(parent=title_bar)
        >>> close_btn.clicked.connect(window.close)
    """

    def __init__(self, parent: Optional[QWidget]) -> None:
        """
        Initialize the close button.

        Args:
            parent (Optional[QWidget]): The parent widget, defaults to None.
        """
        super(CloseButton, self).__init__(parent)

        # Set styling for the close button with red hover effect
        self.setStyleSheet(
            """
        QPushButton {
        	background-position: center;
            background-repeat: no-repeat;
        	border: none;
        	outline: none;
        	color: #d1d3d2;
        }

        QPushButton:hover {
        	background-color: #e81123;
        }"""
        )

        # Set close icon
        self.setIcon(Icon(":/icons/title-bar/close.png"))


class TitleBar(QFrame):
    """
    Windows-specific title bar implementation with custom window controls.

    This class provides a complete title bar for Windows customizable windows,
    including custom window controls (close, minimize, maximize) that match
    the Windows visual style and behavior. The title bar is laid out with
    buttons on the right side and a spacer that takes up the remaining space.

    Features:
    - Custom window controls (close, minimize, maximize/restore)
    - Proper button icons that change based on window state
    - Window dragging by clicking and dragging on the title bar
    - Event filtering to monitor window state changes
    - Responsive layout that adapts to window resizing
    - Native Windows visual styling and behavior

    Attributes:
        button_box (QWidget): Container widget for window control buttons.
        maximize_button (MaximizeButton): The maximize/restore button.
        minimize_button (MinimizeButton): The minimize button.
        close_button (CloseButton): The close button.
        button_box_horizontalLayout (QHBoxLayout): Layout for button container.
        horizontalLayout (QHBoxLayout): Main layout for the title bar.
        horizontalSpacer (QSpacerItem): Spacer that pushes buttons to the right.

    Example:
        >>> title_bar = TitleBar(parent=window)
        >>> window.setTitleBar(title_bar)
    """

    def __init__(self, parent: Optional[QWidget] = None) -> None:
        """
        Initialize the Windows TitleBar.

        Args:
            parent (Optional[QWidget]): The parent widget (usually the window),
                                       defaults to None.
        """
        super(TitleBar, self).__init__(parent)

        self.setObjectName("TitleBar")
        self.setFixedHeight(28)

        self.button_box = QWidget(self)

        self.maximize_button = MaximizeButton(self.button_box)
        self.minimize_button = MinimizeButton(self.button_box)
        self.close_button = CloseButton(self.button_box)

        self.button_box_horizontalLayout = QHBoxLayout(self.button_box)
        self.button_box_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_box_horizontalLayout.setSpacing(0)

        for btn in [self.minimize_button, self.maximize_button, self.close_button]:
            self.button_box_horizontalLayout.addWidget(btn)

        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)

        self.horizontalSpacer = QSpacerItem(
            20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum  # type: ignore
        )  # type: ignore

        self.horizontalLayout.addSpacerItem(self.horizontalSpacer)
        self.horizontalLayout.addWidget(self.button_box)

        self.minimize_button.clicked.connect(self.on_minimize_button_clicked)
        self.maximize_button.clicked.connect(self.on_maximize_button_clicked)
        self.close_button.clicked.connect(self.on_close_button_clicked)

        self.window().installEventFilter(self)

    def on_close_button_clicked(self) -> None:
        """
        Handle close button click event.

        This method is called when the close button is clicked and
        closes the associated window.
        """
        self.window().close()

    def on_maximize_button_clicked(self):
        """Handle maximize button click event."""
        status = self.topLevelWidget().isMaximized()
        if status:
            self.window().showNormal()
            self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
        else:
            self.window().showMaximized()
            self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)

    def on_minimize_button_clicked(self) -> None:
        """
        Handle minimize button click event.

        This method is called when the minimize button is clicked and
        minimizes the associated window.
        """
        self.window().showMinimized()

    def set_maximize_button_icon(self, icon: MaximizeButtonIcon) -> None:
        """Set the maximize button icon based on window state."""
        if icon == MaximizeButtonIcon.MAXIMIZE:
            self.maximize_button.setIcon(Icon(":/icons/title-bar/maximize.png"))
        elif icon == MaximizeButtonIcon.RESTORE:
            self.maximize_button.setIcon(Icon(":/icons/title-bar/restore.png"))

    def eventFilter(self, obj, e):
        """Filter events to monitor window state changes."""
        if obj is self.window():
            if e.type() == QEvent.WindowStateChange:  # type: ignore
                status = self.window().isMaximized()
                if not status:
                    self.set_maximize_button_icon(MaximizeButtonIcon.MAXIMIZE)
                else:
                    self.set_maximize_button_icon(MaximizeButtonIcon.RESTORE)

        return super().eventFilter(obj, e)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Handle mouse move events for window dragging."""
        startSystemMove(self.window(), event.globalPos())
