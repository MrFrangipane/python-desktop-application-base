from PySide6.QtGui import QAction

from pyside6helpers import icons

from desktopapplicationbase._components import _Components
from desktopapplicationbase.actions.component import ActionsComponent
from desktopapplicationbase.actions.handlers.trigger_simple import TriggerSimpleHandler
from desktopapplicationbase.actions.info import ActionInfo
from desktopapplicationbase.application import application_api


def register(action_info: ActionInfo):
    _Components().actions.action_infos.append(action_info)

    new_action = QAction(action_info.icon, action_info.name)
    action_info.handler.q_action = new_action

    if action_info.is_toggle:
        new_action.setCheckable(True)
        new_action.toggled.connect(action_info.handler.toggled)
    else:
        new_action.triggered.connect(action_info.handler.triggered)

    _Components().actions.actions.append(new_action)


def init():
    actions_component = ActionsComponent()
    _Components().actions = actions_component


def register_default_actions():
    # Quit Action always exists
    register(ActionInfo(
        name="&Quit",
        icon=icons.right_arrow(),
        menu_path=["&File"],
        show_in_systray=True,
        handler=TriggerSimpleHandler(application_api.get_instance().quit)
    ))


def get_instance() -> ActionsComponent:
    return _Components().actions
