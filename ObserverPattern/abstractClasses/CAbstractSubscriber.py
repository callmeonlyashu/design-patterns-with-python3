from abc import ABC, abstractmethod


class CSubscriber(ABC):

    def __init__(self):
        super().__init__()

    def update(self, temperature, pressure, humidity):
        pass