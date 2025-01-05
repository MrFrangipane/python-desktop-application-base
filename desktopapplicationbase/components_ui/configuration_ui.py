from dataclasses import dataclass

from PySide6.QtGui import QIcon

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from pyside6helpers import icons


@dataclass
class ConfigurationUi(metaclass=SingletonMetaclass):

    @property
    def icon(self) -> QIcon:
        return icons.diskette()
