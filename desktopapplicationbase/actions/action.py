from PySide6.QtGui import QAction
from dataclasses import dataclass


@dataclass
class Action:
    action: QAction
    menu_path: list[str]
    show_in_systray: bool
