from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class ThickCrustDough(Ingredient):

    def __init__(self):
        super().__init__()
        log.info("Thick Crust Dough is adding to the pizza")