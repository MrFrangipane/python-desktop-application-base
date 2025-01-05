from dataclasses import dataclass

from PySide6.QtWidgets import QApplication, QSystemTrayIcon

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from pyside6helpers.main_window import MainWindow

from desktopapplicationbase.domain_contract_ui.actions import AbstractActions



@dataclass
class ComponentsUi(metaclass=SingletonMetaclass):
    actions: AbstractActions = None
    application: QApplication = None
    main_window: MainWindow = None
    tray_icon: QSystemTrayIcon = None
