from dataclasses import dataclass

from pythonhelpers.singleton_metaclass import SingletonMetaclass


@dataclass
class Configuration(metaclass=SingletonMetaclass):

    @property
    def brand(self) -> str:
        return "Frangitron"

    @property
    def name(self) -> str:
        return "desktopapplicationbase"

    @property
    def title(self) -> str:
        return "Python Desktop Application Base"

    @property
    def project_extension(self) -> str:
        return f"JSON (*.{self.name}.json)"
