from abstractClasses.AbstractFlyBehaviour import FlyBehaviour

class CCanFly( FlyBehaviour ):

    def __init__( self ):
        super().__init__()
    

    def fly(self):
        print("I can fly")