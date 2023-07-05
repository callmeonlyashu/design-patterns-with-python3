from AbstractFactoryPattern.abstractClasses.CAbstractPizzaIngredientFactory import PizzaIngredientFactory
from Ingredients.CThickCrustDough import ThickCrustDough
from Ingredients.CMarinaraSauce import MarinaraSauce
from Ingredients.CVeggies1 import Veggies1
from Ingredients.CVeggies3 import Veggies3
from Ingredients.CMozzarelaCheese import MozzarelaCheese
from config.logger import logger as log


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super().__init__()

    def createDough(self):
        return ThickCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return MozzarelaCheese()

    def createToppings(self):
        return [Veggies1(), Veggies3()]