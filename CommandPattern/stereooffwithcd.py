from config.logger import logger as log
from abstractclasses.command import Command


class StereoOffWithCD(Command):

    def execute(self):
        log.info("Stereo turned off successfully with CD.")

    def undo(self):
        log.info("Stereo turned on successfully with CD")