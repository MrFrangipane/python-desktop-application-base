from dataclasses import dataclass

from pythonhelpers.singleton_metaclass import SingletonMetaclass

from desktopapplicationbase.domain_contract.project_persistence import AbstractProjectPersistence


@dataclass
class Components(metaclass=SingletonMetaclass):
    project_persistence: AbstractProjectPersistence = None
