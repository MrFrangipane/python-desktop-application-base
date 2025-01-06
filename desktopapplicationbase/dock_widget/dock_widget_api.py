from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QWidget

from desktopapplicationbase.main_window import main_window_api


def register_dock_widget(widget: QWidget):
    main_window = main_window_api.get_instance()

    dock_widget = QDockWidget(widget.objectName())
    dock_widget.setWidget(widget)

    main_window.addDockWidget(Qt.RightDockWidgetArea, dock_widget)
