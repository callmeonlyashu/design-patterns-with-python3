from abc import ABC, abstractmethod
from config.logger import logger as log


class Duck(ABC):

    def __init__(self):
        super().__init__()


    #You must implement this in all the subclasses.
    @abstractmethod
    def display(self):
        pass