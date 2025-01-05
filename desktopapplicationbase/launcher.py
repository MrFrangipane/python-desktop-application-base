import sys

from PySide6.QtWidgets import QApplication

from pyside6helpers import css

from desktopapplicationbase.components.components import Components
from desktopapplicationbase.components.project_persistence import ProjectPersistence

from desktopapplicationbase.components_ui.actions import Actions
from desktopapplicationbase.components_ui.components_ui import ComponentsUi
from desktopapplicationbase.components_ui.main_window_factory import create_main_window
from desktopapplicationbase.components_ui.system_tray_icon_factory import create_system_tray_icon


class Launcher:

    def __init__(self):
        # TODO instantiate all components
        Components().project_persistence = ProjectPersistence()

    def exec(self):
        app = QApplication()

        # TODO instantiate all Ui components

        ComponentsUi().actions = Actions()
        ComponentsUi().actions.create_actions(app)

        ComponentsUi().system_tray_icon = create_system_tray_icon()
        ComponentsUi().system_tray_icon.show()

        css.load_onto(app)
        app.setQuitOnLastWindowClosed(False)
        app.aboutToQuit.connect(lambda: None)  # TODO replace lambda with actual code if needed

        create_main_window(app)
        ComponentsUi().main_window.show()

        sys.exit(app.exec())
