from abstractClasses.AbstractFlyBehaviour import FlyBehaviour
from config.logger import logger as log


class CCannotFly( FlyBehaviour ):

    def __init__( self ):
        super().__init__()

    def fly(self):
        log.info("I can not fly")