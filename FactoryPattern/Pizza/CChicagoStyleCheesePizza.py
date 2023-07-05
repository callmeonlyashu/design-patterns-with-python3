from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        self.toppings = ["Cheese", "Mozarrela Cheese"]
        super().__init__()
        log.info("Chicago Style Cheese Pizza Creating...")
