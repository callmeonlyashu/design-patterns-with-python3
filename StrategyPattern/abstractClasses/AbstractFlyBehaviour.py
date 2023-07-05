from abc import ABC, abstractmethod
from config.logger import logger as log


class FlyBehaviour(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def fly(self):
        pass