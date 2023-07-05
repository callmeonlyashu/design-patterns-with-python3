from AbstractFactoryPattern.abstractClasses.CAbstractIngredients import Ingredient
from config.logger import logger as log


class MarinaraSauce(Ingredient):
    
    def __init__(self):
        super().__init__()
        log.info("Marinara Sauce is adding to the pizza")