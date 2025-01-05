from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from pyside6helpers.main_window import MainWindow

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from desktopapplicationbase.configuration.configuration import Configuration


class Components(metaclass=SingletonMetaclass):
    def __init__(self):
        self.application: QApplication = None
        self.configuration: Configuration = None
        self.main_window: MainWindow = None
        self.systray_icon: QSystemTrayIcon = None
