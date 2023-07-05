from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CRocketFly import CRocketFly
from quackBehaviour.CMallockQuack import CMallokQuack
from config.logger import logger as log


class CMallokDuck(Duck):

    def __init__(self):
        super().__init__()
        self.flyBehaviour = CRocketFly()
        self.quackBehaviour = CMallokQuack()

    def display(self):
        log.info("I am the Mallock duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour(self):
        self.quackBehaviour.quack()