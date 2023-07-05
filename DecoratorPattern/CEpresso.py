from abstractClasses.CAbstractBevarages import Bevarages
from config.logger import logger as log


class Epresso( Bevarages ):

    def __init__(self):
        super().__init__()

    def description(self):
        return "Epresso"

    def price(self):
        return 60
