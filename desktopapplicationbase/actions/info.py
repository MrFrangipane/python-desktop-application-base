from PySide6.QtGui import QIcon
from dataclasses import dataclass

from desktopapplicationbase.actions.handlers.abstract import ActionAbstractHandler


@dataclass
class ActionInfo:
    handler: ActionAbstractHandler
    icon: QIcon
    menu_path: list[str]
    name: str
    show_in_systray: bool
    is_toggle: bool = False
