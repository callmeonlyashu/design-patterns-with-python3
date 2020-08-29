from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCannotFly import CCannotFly
from quackBehaviour.CCanQuack import CCanQuack

class CRubberDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCannotFly()
        self.quackBehaviour = CCanQuack()
    

    def display(self):
        print("I am the rubber duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()