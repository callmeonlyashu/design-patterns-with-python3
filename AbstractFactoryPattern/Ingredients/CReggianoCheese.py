from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class ReggianoCheese(Ingredient):

    def __init__(self):
        super().__init__()
        log.info("Reggiano Cheese is adding to the pizza")