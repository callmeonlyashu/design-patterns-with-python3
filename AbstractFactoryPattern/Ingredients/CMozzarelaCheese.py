from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class MozzarelaCheese(Ingredient):

    def __init__(self):
        super().__init__()
        log.info("Mozzarela Cheese is adding to the pizza")