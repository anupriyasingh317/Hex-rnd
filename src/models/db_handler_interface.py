from abc import ABC, abstractmethod

class DBHandlerInterface(ABC):
    @abstractmethod
    def insert_event(self, event):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def create_table(self):
        pass
