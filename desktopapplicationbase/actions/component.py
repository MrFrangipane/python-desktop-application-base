from PySide6.QtGui import QAction

from desktopapplicationbase.actions.info import ActionInfo


class ActionsComponent:
    def __init__(self):
        self.action_infos: list[ActionInfo] = list()
        self.actions: list[QAction] = list()
