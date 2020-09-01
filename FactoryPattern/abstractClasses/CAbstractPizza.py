from abc import ABC, abstractmethod
class Pizza(ABC):

    def __init__(self):
        super().__init__()

    def prepare(self):
        print("Preparing...")

    def bake(self):
        print("Baking...")

    def cut(self):
        print("Cutting...")

    def box(self):
        print("Adding to the Box...")