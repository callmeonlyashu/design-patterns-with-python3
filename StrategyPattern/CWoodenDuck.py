from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCannotFly import CCannotFly
from quackBehaviour.CCannotQuack import CCannotQuack
from config.logger import logger as log


class CWoodenDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCannotFly()
        self.quackBehaviour = CCannotQuack()

    def display(self):
        log.info("I am the wooden duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()