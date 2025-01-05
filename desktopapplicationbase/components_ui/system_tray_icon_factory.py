from PySide6.QtWidgets import QMenu, QSystemTrayIcon

from desktopapplicationbase.components_ui.components_ui import ComponentsUi
from desktopapplicationbase.components_ui.configuration_ui import ConfigurationUi


def _on_tray_icon_activated(reason):
    if reason == QSystemTrayIcon.ActivationReason.Trigger:
        ComponentsUi().main_window.showNormal()
        ComponentsUi().main_window.activateWindow()


def create_system_tray_icon() -> QSystemTrayIcon:
    menu = QMenu()
    menu.addAction(ComponentsUi().actions.quit)

    tray_icon = QSystemTrayIcon(ConfigurationUi().icon, ComponentsUi().application)
    tray_icon.setContextMenu(menu)
    tray_icon.activated.connect(_on_tray_icon_activated)

    return tray_icon
