from abc import ABC, abstractmethod
from config.logger import logger as log


class Command(ABC):

    def __init__(self):
        super().__init__()

    """
    Abstract Functions that we need to extend in the sub-classes.
    """
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass