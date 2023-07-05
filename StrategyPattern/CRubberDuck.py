from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCannotFly import CCannotFly
from quackBehaviour.CCanQuack import CCanQuack
from config.logger import logger as log


class CRubberDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCannotFly()
        self.quackBehaviour = CCanQuack()

    def display(self):
        log.info("I am the rubber duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()