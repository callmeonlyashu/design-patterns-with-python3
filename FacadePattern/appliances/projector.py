from config.logger import logger as log


class Projector():

    def __init__(self):
        super().__init__()

    def turn_on(self):
        log.info("Projector has been turned On")

    def turn_off(self):
        log.info("Projector has been turned Off")