from ..abstractClasses.AbstractQuackBehaviour import QuackBehaviour

class CCanQuack( QuackBehaviour ):

    def __init__( self ):
        super().__init__()
    

    def quack(self):
        print("I can speak")