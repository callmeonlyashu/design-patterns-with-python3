from abstractClasses import CAbstractSubscriber as subscriber
from abstractClasses import CAbstractDisplay as display
from config.logger import logger as log


class WeatherMobileSubscriber(subscriber.CSubscriber, display.CDisplay):

    def __init__(self, sub):
        super().__init__()
        self.weatherinfo = sub
        sub.registerSubscriber(self)

    def update(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.display()

    def display(self):
        log.info("Current conditions of mobile weather are temp - {}, humidity - {}, pressure - {}".format(self.temperature, self.humidity, self.pressure))
