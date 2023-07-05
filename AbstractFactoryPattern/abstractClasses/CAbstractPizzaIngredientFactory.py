from abc import ABC, abstractmethod
from config.logger import logger as log


class PizzaIngredientFactory(ABC):

    def __init__(self):
        super().__init__()

    def createDough(self):
        pass

    def createSauce(self):
        pass

    def createCheese(self):
        pass

    def createToppings(self):
        pass