from abstractclasses.abstractduck import Duck
from config.logger import logger as log


class MallardDuck(Duck):

    def __init__(self):
        super().__init__()

    def quack(self):
        log.info("I can Quack like Mallard Duck")

    def fly(self):
        log.info("I can Fly like Mallard Duck")
