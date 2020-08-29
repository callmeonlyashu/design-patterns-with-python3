from abc import ABC, abstractmethod
class Duck(ABC):

    def __init__(self):
        super().__init__()


    #You must implement this in all the subclasses.
    @abstractmethod
    def display(self):
        pass