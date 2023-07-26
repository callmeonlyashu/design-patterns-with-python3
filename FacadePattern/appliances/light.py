from config.logger import logger as log


class Light():

    def __init__(self):
        super().__init__()

    def turn_on(self):
        log.info("Light has been turned On")

    def turn_off(self):
        log.info("Light has been turned Off")
        
    def dim(self, point):
        log.info("Light is dim to {}".format(point))