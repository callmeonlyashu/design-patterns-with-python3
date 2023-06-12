from abstractClasses.AbstractQuackBehaviour import QuackBehaviour

class CCannotQuack( QuackBehaviour ):

    def __init__( self ):
        super().__init__()
    

    def quack(self):
        print("I can not speak")