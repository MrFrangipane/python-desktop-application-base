from abc import ABCMeta, ABC, abstractmethod

from PySide6.QtCore import QObject
from PySide6.QtWidgets import QApplication


class _MetaQObjectABC(ABCMeta, type(QObject)):
    pass


class AbstractActions(ABC, QObject, metaclass=_MetaQObjectABC):
    def __init__(self, parent=None):
        super().__init__(parent)

    @abstractmethod
    def create_actions(self, app: QApplication):
        pass
