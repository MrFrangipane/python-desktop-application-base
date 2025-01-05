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


def show() -> None:
    Components().main_window.show()
