from abc import ABC

from PySide6.QtGui import QAction


class ActionAbstractHandler(ABC):

    def __init__(self):
        self.q_action: QAction = None

    def toggled(self):
        pass

    def triggered(self):
        pass
