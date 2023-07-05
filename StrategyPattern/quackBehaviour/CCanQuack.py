from abstractClasses.AbstractQuackBehaviour import QuackBehaviour
from config.logger import logger as log


class CCanQuack( QuackBehaviour ):

    def __init__( self ):
        super().__init__()

    def quack(self):
        log.info("I can speak")