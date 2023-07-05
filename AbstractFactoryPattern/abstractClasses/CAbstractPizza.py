from abc import ABC, abstractmethod
from config.logger import logger as log
from AbstractFactoryPattern.abstractClasses.CAbstractPizzaIngredientFactory import PizzaIngredientFactory


class Pizza(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        log.info("Bake for 20 mins at 250C...")

    def cut(self):
        log.info("Cut the pizza into hexagonal pieces")

    def box(self):
        log.info("Place the pizza in official pizza store box.")