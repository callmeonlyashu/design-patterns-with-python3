from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log


class NYStyleCheesePizza(Pizza):

    def __init__(self):
        self.toppings = ["Cheese", "Mozarrela Cheese"]
        super().__init__()
        log.info("NY Style Cheese Pizza Creating...")
