from abstractClasses.AbstractFlyBehaviour import FlyBehaviour

class CCannotFly( FlyBehaviour ):

    def __init__( self ):
        super().__init__()
    

    def fly(self):
        print("I can not fly")