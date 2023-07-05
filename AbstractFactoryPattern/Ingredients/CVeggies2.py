from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class Veggies2(Ingredient):

    def __init__(self):
        super().__init__()
        log.info("Veggies2 is adding to the pizza")