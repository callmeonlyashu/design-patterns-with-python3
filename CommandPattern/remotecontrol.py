from config.logger import logger as log


class RemoteControl():

    def __init__(self):
        self.onCommands = {}
        self.offCommands = {}

    def set_command(self, slot, oncommand, offcommand):
        self.onCommands[slot] = oncommand
        self.offCommands[slot] = offcommand

    def on_button_push(self, slot):
        self.onCommands[slot].execute()

    def off_button_push(self, slot):
        self.offCommands[slot].execute()