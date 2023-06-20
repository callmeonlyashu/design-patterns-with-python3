from abstractClasses import CAbstractPublisher as publisher
from config.logger import logger as log


class Weather(publisher.CPublisher):

    def __init__(self):
        super().__init__()
        self.subscribers = []

    def registerSubscriber(self, subscribers):
        self.subscribers.append(subscribers)
        log.info("{} added successfully to the list".format(subscribers))
        return self.subscribers

    def removeSubscriber(self, subscribers):
        self.subscribers.remove(subscribers)
        log.info("{} removed successfully from the list".format(subscribers))
        return self.subscribers

    def notifySubscriber(self):
        for subscriber in self.subscribers:
            log.info("{} notified successfully.".format(subscriber))
            subscriber.update(self.temperature, self.humidity, self.pressure)

    def measurementChanged(self):
        log.info("notifying the subscribers....")
        self.notifySubscriber()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurementChanged()

