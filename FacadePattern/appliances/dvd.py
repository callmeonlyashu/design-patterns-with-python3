from config.logger import logger as log


class Dvd():

    def __init__(self):
        super().__init__()

    def turn_on(self):
        log.info("DVD has been turned On")

    def turn_off(self):
        log.info("DVD has been turned Off")

    def setmovie(self, movie):
        log.info("{} is set to play mode.".format(movie))