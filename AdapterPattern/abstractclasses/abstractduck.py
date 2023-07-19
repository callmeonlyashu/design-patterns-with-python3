from abc import ABC, abstractmethod
from config.logger import logger as log


class Duck(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def quack(self):
        pass

    @abstractmethod
    def fly(self):
        pass
