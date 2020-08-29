from abstractClasses.AbstractDuck import Duck
from flyBehaviour.CCanFly import CCanFly
from quackBehaviour.CCanQuack import CCanQuack

class CRealDuck( Duck ):

    def __init__( self ):
        super().__init__()
        self.flyBehaviour = CCanFly()
        self.quackBehaviour = CCanQuack()
    

    def display(self):
        print("I am the real duck")

    def getFlyBehaviour(self):
        self.flyBehaviour.fly()

    def getQuackBehaviour( self ):
        self.quackBehaviour.quack()