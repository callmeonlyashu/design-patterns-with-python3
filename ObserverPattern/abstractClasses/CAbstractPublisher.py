from abc import ABC, abstractmethod


class CPublisher(ABC):

    def __init__(self):
        super().__init__()

    def registerSubscriber(self, subscribers):
        pass

    def removeSubscriber(self, subscribers):
        pass

    def notifySubscriber(self):
        pass