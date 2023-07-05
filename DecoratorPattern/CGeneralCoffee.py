from abstractClasses.CAbstractBevarages import Bevarages
from config.logger import logger as log


class GeneralCoffee( Bevarages ):

    def __init__(self):
        super().__init__()

    def description(self):
        return "General Coffee"

    def price(self):
        return 50
