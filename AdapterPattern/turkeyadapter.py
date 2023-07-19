from abstractclasses.abstractduck import Duck
from config.logger import logger as log


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        super().__init__()
        self.turkey = turkey

    def quack(self):
        log.info("Quacking from the Adapter")
        self.turkey.gobble()

    def fly(self):
        log.info("Flying from the adapter")
        self.turkey.fly()
