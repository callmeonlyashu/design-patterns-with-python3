from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCannotFly import CCannotFly
from quackBehaviour.CCannotQuack import CCannotQuack

class CWoodenDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCannotFly()
        self.quackBehaviour = CCannotQuack()
    

    def display(self):
        print("I am the wooden duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()