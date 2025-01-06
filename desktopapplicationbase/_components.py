from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from pyside6helpers.main_window import MainWindow

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from desktopapplicationbase.actions.component import ActionsComponent
from desktopapplicationbase.configuration.info import ConfigurationInfo


class _Components(metaclass=SingletonMetaclass):
    def __init__(self):
        self.configuration: ConfigurationInfo = None

        self.actions: ActionsComponent = None
        self.application: QApplication = None
        self.main_window: MainWindow = None
        self.systray_icon: QSystemTrayIcon = None
