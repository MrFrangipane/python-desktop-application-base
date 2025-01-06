from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from desktopapplicationbase._components import _Components
from desktopapplicationbase.actions import actions_api
from desktopapplicationbase.application import application_api
from desktopapplicationbase.configuration import configuration_api
from desktopapplicationbase.main_window import main_window_api


def init() -> None:
    configuration = configuration_api.get()
    if not configuration.has_systray_icon:
        return

    systray_icon = QSystemTrayIcon(QIcon(configuration.icon_filepath), application_api.get_instance())

    menu = QMenu()
    actions_component = actions_api.get_instance()
    for action_info, action in zip(actions_component.action_infos, actions_component.actions):
        if action_info.show_in_systray:
            menu.addAction(action)

    systray_icon.setContextMenu(menu)

    main_window = main_window_api.get_instance()
    if main_window is None:
        raise ValueError("Main window is not set")
    systray_icon.activated.connect(main_window.show)

    _Components().systray_icon = systray_icon


def show() -> None:
    if _Components().systray_icon is None:
        return

    _Components().systray_icon.show()
