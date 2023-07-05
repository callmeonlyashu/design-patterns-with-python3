from abc import ABC, abstractmethod
from config.logger import logger as log


class Bevarages(ABC):

    def __init__(self):
        super().__init__()

    """
    Abstract Functions that we need to extend in the sub-classes.
    """
    @abstractmethod
    def description(self):
        pass

    @abstractmethod
    def price(self):
        pass