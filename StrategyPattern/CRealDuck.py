from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCanFly import CCanFly
from quackBehaviour.CCanQuack import CCanQuack
from config.logger import logger as log


class CRealDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCanFly()
        self.quackBehaviour = CCanQuack()

    def display(self):
        log.info("I am the real duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()