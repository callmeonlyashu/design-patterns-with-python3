from config.logger import logger as log


class Speaker():

    def __init__(self):
        super().__init__()

    def turn_on(self):
        log.info("Speaker has been turned On")

    def turn_off(self):
        log.info("Speaker has been turned Off")

    def setvolume(self, volume):
        log.info("Speaker has been set to volume 20")
