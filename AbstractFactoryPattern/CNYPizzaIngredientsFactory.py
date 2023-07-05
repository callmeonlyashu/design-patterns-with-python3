from AbstractFactoryPattern.abstractClasses.CAbstractPizzaIngredientFactory import PizzaIngredientFactory
from Ingredients.CThinCrustDough import ThinCrustDough
from Ingredients.CMarinaraSauce import MarinaraSauce
from Ingredients.CVeggies1 import Veggies1
from Ingredients.CVeggies2 import Veggies2
from Ingredients.CReggianoCheese import ReggianoCheese
from config.logger import logger as log


class NyPizzaIngredientFactory(PizzaIngredientFactory):

    def __init__(self):
        super().__init__()

    def createDough(self):
        return ThinCrustDough()

    def createSauce(self):
        return MarinaraSauce()

    def createCheese(self):
        return ReggianoCheese()

    def createToppings(self):
        return [Veggies1(), Veggies2()]