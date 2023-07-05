from abstractClasses.AbstractQuackBehaviour import QuackBehaviour
from config.logger import logger as log


class CCannotQuack( QuackBehaviour ):

    def __init__( self ):
        super().__init__()

    def quack(self):
        log.info("I can not speak")