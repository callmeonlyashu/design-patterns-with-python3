from abstractClasses import CAbstractSubscriber as subscriber
from abstractClasses import CAbstractDisplay as display
from config.logger import logger as log


class WeatherMonitorSubscriber(subscriber.CSubscriber, display.CDisplay):

    def __init__(self, publisher):
        super().__init__()
        self.weatherinfo = publisher
        publisher.registerSubscriber(self)
        log.info("Weather Monitor subscriber as been initiated")

    def update(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity
        self.display()

    def display(self):
        log.info("Current conditions of monitor weather are temp - {}, humidity - {}, pressure - {}".format(self.temperature, self.humidity, self.pressure))
