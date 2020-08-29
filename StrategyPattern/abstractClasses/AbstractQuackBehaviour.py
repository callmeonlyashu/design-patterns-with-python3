from abc import ABC, abstractmethod
class QuackBehaviour(ABC):

    def __init__(self):
        super().__init__()


    #You must implement this in all the subclasses.
    @abstractmethod
    def quack(self):
        pass