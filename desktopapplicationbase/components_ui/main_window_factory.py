from PySide6.QtWidgets import QApplication

from pyside6helpers.main_window import MainWindow

from desktopapplicationbase.apis import project_persistence

from desktopapplicationbase.components.configuration import Configuration
from desktopapplicationbase.components.resources import Resources

from desktopapplicationbase.components_ui.central_widget import CentralWidget
from desktopapplicationbase.components_ui.components_ui import ComponentsUi
from desktopapplicationbase.components_ui.configuration_ui import ConfigurationUi


def create_main_window(app: QApplication):
    main_window = MainWindow(
        logo_filepath=Resources().make_path("frangitron-logo.png"),
        settings_tuple=("Frangitron", Configuration().title),
    )
    main_window.setWindowTitle(Configuration().title)
    main_window.setWindowIcon(ConfigurationUi().icon)
    main_window.setCentralWidget(CentralWidget())
    main_window.shown.connect(project_persistence.open_last_saved)

    menu_bar = main_window.menuBar()
    file_menu = menu_bar.addMenu("&File")
    file_menu.addAction(ComponentsUi().actions.new)
    file_menu.addAction(ComponentsUi().actions.open)
    file_menu.addAction(ComponentsUi().actions.save)
    file_menu.addSeparator()
    file_menu.addAction(ComponentsUi().actions.quit)

    ComponentsUi().main_window = main_window
