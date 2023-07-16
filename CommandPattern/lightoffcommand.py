from config.logger import logger as log
from abstractclasses.command import Command


class LightOffCommand(Command):

    def execute(self):
        log.info("Light has been turned Off successfully.")

    def undo(self):
        log.info("Light has been turned On successfully")