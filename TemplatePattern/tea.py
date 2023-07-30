from config.logger import logger as log
from abstractclasses.caffeinebeveragewithhook import CaffeineBeverageWithHook


class Tea(CaffeineBeverageWithHook):
    def __init__(self):
        super().__init__()

    def brew(self):
        log.info("Tea Red Label added as a brew")

    def add_condiments(self):
        log.info("Adding sugar, milk and other condiments")



