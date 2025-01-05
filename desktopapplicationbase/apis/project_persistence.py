from PySide6.QtCore import QSettings

from desktopapplicationbase.components.components import Components
from desktopapplicationbase.components.configuration import Configuration
from desktopapplicationbase.components_ui.components_ui import ComponentsUi


def new():
    Components().project_persistence.reset()
    # TODO add some ComponentsUi() calls if needed


def open_last_saved():
    settings = QSettings(Configuration().brand, Configuration().title)
    filepath = settings.value('last_saved_project')
    open_(filepath)
    # TODO add some ComponentsUi() calls if needed


def open_(filepath):
    Components().project_persistence.open(filepath)
    # TODO add some ComponentsUi() calls if needed


def save(filepath):
    Components().project_persistence.save(filepath)
    settings = QSettings(Configuration().brand, Configuration().title)
    settings.setValue('last_saved_project', filepath)
    # TODO add some ComponentsUi() calls if needed
