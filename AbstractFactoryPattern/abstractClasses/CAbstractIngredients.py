from abc import ABC, abstractmethod
from config.logger import logger as log


class Ingredient(ABC):

    def __init__(self):
        super().__init__()
        log.info("Adding Ingredients")