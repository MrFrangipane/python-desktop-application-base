from PySide6.QtGui import QAction

from pyside6helpers import icons

from desktopapplicationbase.actions.action_info import ActionInfo
from desktopapplicationbase.actions.actions import Actions
from desktopapplicationbase.components import Components
from desktopapplicationbase.actions.handlers.trigger_simple import TriggerSimpleHandler


def register(action_info: ActionInfo):
    Components().actions.action_infos.append(action_info)

    new_action = QAction(action_info.icon, action_info.name)
    action_info.handler.q_action = new_action

    if action_info.is_toggle:
        new_action.setCheckable(True)
        new_action.toggled.connect(action_info.handler.toggled)
    else:
        new_action.triggered.connect(action_info.handler.triggered)

    Components().actions.actions.append(new_action)


def init():
    actions = Actions()
    Components().actions = actions


def register_default_actions():
    # Quit Action always exists
    register(ActionInfo(
        name="&Quit",
        icon=icons.right_arrow(),
        menu_path=["&File"],
        show_in_systray=True,
        handler=TriggerSimpleHandler(Components().application.quit)
    ))
