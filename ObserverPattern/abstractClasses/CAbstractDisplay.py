from abc import ABC, abstractmethod


class CDisplay(ABC):

    def __init__(self):
        super().__init__()

    def display(self):
        pass