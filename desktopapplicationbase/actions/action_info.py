from PySide6.QtGui import QIcon
from dataclasses import dataclass


@dataclass
class ActionInfo:
    name: str
    icon: QIcon
    menu_path: list[str]
    show_in_systray: bool
    checkable: bool = False
    triggered: callable = None
    toggled: callable = None
