from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from pyside6helpers.main_window import MainWindow

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from desktopapplicationbase.configuration.configuration import Configuration
from desktopapplicationbase.actions.actions import Actions


class Components(metaclass=SingletonMetaclass):
    def __init__(self):
        self.configuration: Configuration = None

        self.actions: Actions = None
        self.application: QApplication = None
        self.main_window: MainWindow = None
        self.systray_icon: QSystemTrayIcon = None
