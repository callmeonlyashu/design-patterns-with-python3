from abc import ABC, abstractmethod
from config.logger import logger as log


class Pizza(ABC):

    def __init__(self):
        super().__init__()
        log.info("Adding sauce")
        log.info("Tossing dough")
        log.info("Adding toppings")
        if self.toppings is not None:
            for topping in self.toppings:
                log.info("Added {} topping".format(topping))

    def prepare(self):
        log.info("Preparing the pizza...")

    def bake(self):
        log.info("Bake for 20 mins at 250C...")

    def cut(self):
        log.info("Cut the pizza into hexagonal pieces")

    def box(self):
        log.info("Place the pizza in official pizza store box.")