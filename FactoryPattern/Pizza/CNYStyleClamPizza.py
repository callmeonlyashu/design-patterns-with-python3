from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log


class NYStyleClamPizza(Pizza):

    def __init__( self ):
        self.toppings = ["Cheese", "Mozarrela Cheese", "Clam"]
        super().__init__()
        log.info("NY Style Clam Pizza Creating...")
