from config.logger import logger as log
from abstractclasses.command import Command


class LightOnCommand(Command):

    def execute(self):
        log.info("Light has been turned On successfully.")

    def undo(self):
        log.info("Light has been turned Off successfully")