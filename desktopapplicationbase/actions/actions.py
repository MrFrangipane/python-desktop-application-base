from PySide6.QtGui import QAction

from desktopapplicationbase.actions.action_info import ActionInfo


class Actions:
    def __init__(self):
        self.action_infos: list[ActionInfo] = list()
        self.actions: list[QAction] = list()
