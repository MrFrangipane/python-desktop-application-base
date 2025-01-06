import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers import css

from desktopapplicationbase._components import _Components
from desktopapplicationbase.configuration import configuration_api


def init() -> None:
    application = QApplication([])
    css.load_onto(application)
    configuration = configuration_api.get()

    if configuration.has_systray_icon:
        application.setQuitOnLastWindowClosed(False)

    _Components().application = application


def exec_() -> None:
    sys.exit(_Components().application.exec())


def get_instance() -> QApplication:
    return _Components().application
