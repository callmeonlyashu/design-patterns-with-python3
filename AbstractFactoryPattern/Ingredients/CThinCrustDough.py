from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class ThinCrustDough(Ingredient):

    def __init__(self):
        super().__init__()
        log.info("Thin Crust Dough is adding to the pizza")