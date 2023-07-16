from config.logger import logger as log
from abstractclasses.command import Command


class StereoOnWithCD(Command):

    def execute(self):
        log.info("Stereo turned on successfully.")
        log.info("Stereo set to work with CD.")
        log.info("Stereo volume set to 11.")

    def undo(self):
        log.info("Stereo turned off successfully with CD")