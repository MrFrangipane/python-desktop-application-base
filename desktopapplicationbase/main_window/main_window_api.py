from PySide6.QtGui import QIcon

from pyside6helpers.main_window import MainWindow

from desktopapplicationbase._components import _Components
from desktopapplicationbase.actions import actions_api
from desktopapplicationbase.configuration import configuration_api


def init() -> None:
    configuration = configuration_api.get()
    main_window = MainWindow(
        logo_filepath=configuration.status_bar_logo_filepath,
        settings_tuple=(configuration.brand, configuration.name)
    )
    main_window.setWindowTitle(configuration.name)
    main_window.setWindowIcon(QIcon(configuration.icon_filepath))
    _Components().main_window = main_window

    menu_bar = main_window.menuBar()
    menus = dict()

    for action_info, action in zip(actions_api.get_instance().action_infos, actions_api.get_instance().actions):
        menu_path = str(action_info.menu_path)  # FIXME : hacky and only one level of depth
        if menu_path:
            if menu_path not in menus.keys():
                menus[menu_path] = menu_bar.addMenu(action_info.menu_path[0])

            menus[menu_path].addAction(action)


def show() -> None:
    _Components().main_window.show()


def get_instance() -> MainWindow:
    main_window = _Components().main_window
    if main_window is None:
        raise ValueError("Main window is not set")
    return main_window
