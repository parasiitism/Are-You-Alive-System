from abc import ABC, abstractmethod
class Notifier(ABC):
    """
    Base class for all notification channels
    """

    @abstractmethod
    def send(self,user,message: str):
        pass
