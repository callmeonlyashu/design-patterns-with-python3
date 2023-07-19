from abstractclasses.abstractturkey import Turkey
from config.logger import logger as log


class WildTurkey(Turkey):

    def __init__(self):
        super().__init__()

    def gobble(self):
        log.info("I can gobble like Wild Turkey")

    def fly(self):
        log.info("I can Fly like Wild Turkey")
