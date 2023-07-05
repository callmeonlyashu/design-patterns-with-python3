from abstractClasses.AbstractQuackBehaviour import QuackBehaviour
from config.logger import logger as log


class CMallokQuack(QuackBehaviour):

    def __init__(self):
        super().__init__()

    def quack(self):
        log.info("I can speak like a Mallok Duck")