from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self):
        self.toppings = ["Cheese", "Mozarrela Cheese", "Veggies"]
        super().__init__()
        log.info("Chicago Style Cheese Pizza Creating...")
