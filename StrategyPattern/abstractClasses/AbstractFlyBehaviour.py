from abc import ABC, abstractmethod
class FlyBehaviour(ABC):

    def __init__(self):
        super().__init__()


    #You must implement this in all the subclasses.
    @abstractmethod
    def fly(self):
        pass