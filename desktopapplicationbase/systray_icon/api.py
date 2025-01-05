from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from desktopapplicationbase.components import Components
from desktopapplicationbase.configuration import api as configuration_api


def make() -> None:
    configuration = configuration_api.get()
    if not configuration.has_systray_icon:
        return

    systray_icon = QSystemTrayIcon(QIcon(configuration.icon_filepath), Components().application)

    menu = QMenu()
    action_exit = menu.addAction("Exit")
    action_exit.triggered.connect(Components().application.quit)

    systray_icon.setContextMenu(menu)

    Components().systray_icon = systray_icon


def show() -> None:
    if Components().systray_icon is None:
        return

    Components().systray_icon.show()
