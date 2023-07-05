from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log


class ChicagoStyleClamPizza(Pizza):

    def __init__(self):
        self.toppings = ["Cheese", "Mozarrela Cheese", "clam"]
        super().__init__()
        log.info("Chicago Style Cheese Pizza Creating...")
