from config.logger import logger as log
from appliances.light import Light
from appliances.speaker import Speaker
from appliances.projector import Projector
from appliances.dvd import Dvd


class HomeTheatreFacade():

    def __init__(self):
        super().__init__()
        self.objlight = Light()
        self.objspeaker = Speaker()
        self.objprojector = Projector()
        self.objdvd = Dvd()

    def start_home_theatre(self):
        log.info("Home Theatre Starting")
        self.objlight.turn_on()
        self.objlight.dim(22)
        self.objspeaker.turn_on()
        self.objspeaker.setvolume(30)
        self.objprojector.turn_on()
        self.objdvd.turn_on()
        self.objdvd.setmovie("Taare Zameen Par")

    def stop_home_theatre(self):
        log.info("Home Theatre Stopping")
        self.objlight.dim(0)
        self.objlight.turn_off()
        self.objspeaker.setvolume(0)
        self.objspeaker.turn_off()
        self.objprojector.turn_off()
        self.objdvd.turn_off()
