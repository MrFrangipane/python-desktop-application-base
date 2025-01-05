import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers import css

from desktopapplicationbase.configuration import api as configuration_api
from desktopapplicationbase.components import Components


def make() -> None:
    application = QApplication([])
    css.load_onto(application)
    configuration = configuration_api.get()

    if configuration.has_systray_icon:
        application.setQuitOnLastWindowClosed(False)

    Components().application = application


def exec_() -> None:
    sys.exit(Components().application.exec())
