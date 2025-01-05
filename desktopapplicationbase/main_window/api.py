from PySide6.QtGui import QIcon

from pyside6helpers.main_window import MainWindow

from desktopapplicationbase.components import Components
from desktopapplicationbase.configuration import api as configuration_api


def make() -> None:
    configuration = configuration_api.get()
    main_window = MainWindow(
        logo_filepath=configuration.status_bar_logo_filepath,
        settings_tuple=(configuration.brand, configuration.name)
    )
    main_window.setWindowTitle(configuration.name)
    main_window.setWindowIcon(QIcon(configuration.icon_filepath))
    Components().main_window = main_window

    menu_bar = main_window.menuBar()
    menus = dict()

    for action_info, action in zip(Components().actions.action_infos, Components().actions.actions):
        menu_path = str(action_info.menu_path)  # FIXME : hacky and only one level of depth
        if menu_path:
            if menu_path not in menus.keys():
                menus[menu_path] = menu_bar.addMenu(action_info.menu_path[0])

            menus[menu_path].addAction(action)


def show() -> None:
    Components().main_window.show()
