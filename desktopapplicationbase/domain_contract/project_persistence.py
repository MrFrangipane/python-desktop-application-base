from abc import ABC, abstractmethod


class AbstractProjectPersistence(ABC):

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def open(self, filepath):
        pass

    @abstractmethod
    def save(self, filepath):
        pass
