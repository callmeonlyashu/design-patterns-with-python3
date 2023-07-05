from abstractClasses.AbstractFlyBehaviour import FlyBehaviour
from config.logger import logger as log


class CCanFly( FlyBehaviour ):

    def __init__( self ):
        super().__init__()

    def fly(self):
        log.info("I can fly")