from config.logger import logger as log
from CommandPattern.lightoncommand import LightOnCommand
from CommandPattern.lightoffcommand import LightOffCommand
from CommandPattern.stereoonwithcd import StereoOnWithCD
from CommandPattern.stereooffwithcd import StereoOffWithCD
from remotecontrol import RemoteControl


lighton = LightOnCommand()
lightoff = LightOffCommand()
stereoon = StereoOnWithCD()
stereooff = StereoOffWithCD()


remote_control = RemoteControl()
remote_control.set_command(0, lighton, lightoff)
remote_control.set_command(1, stereoon, stereooff)

log.info("Remote is set to use")

remote_control.on_button_push(0)
remote_control.on_button_push(1)
remote_control.off_button_push(0)
remote_control.off_button_push(1)




