from PySide6.QtGui import QAction

from pyside6helpers import icons

from desktopapplicationbase.actions.action import Action
from desktopapplicationbase.actions.actions import Actions
from desktopapplicationbase.components import Components


def make():
    actions = Actions()

    quit_action = Action(
        action=QAction(icons.right_arrow(), "&Quit"),
        menu_path=["&File"],
        show_in_systray=True
    )
    quit_action.action.triggered.connect(Components().application.quit)
    actions.actions.append(quit_action)

    Components().actions = actions
