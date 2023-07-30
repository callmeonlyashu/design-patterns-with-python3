from config.logger import logger as log
from abc import ABC, abstractmethod


class CaffeineBeverageWithHook(ABC):
    def __init__(self):
        pass

    def prepare_recipe(self, customerwantscondiments):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.customerwantscondiments(customerwantscondiments)

    def boil_water(self):
        log.info("Water boiling has been started")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def pour_in_cup(self):
        log.info("Pouring in the cup")

    def customerwantscondiments(self, customerwantscondiments):
        if customerwantscondiments:
            self.add_condiments()
        else:
            log.info("Serving without condiments")




