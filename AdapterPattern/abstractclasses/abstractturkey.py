from abc import ABC, abstractmethod
from config.logger import logger as log


class Turkey(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass
