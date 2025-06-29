from abc import ABC, abstractmethod


class Collection(ABC):
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def all(self):
        pass