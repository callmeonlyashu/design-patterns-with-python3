from config.logger import logger as log
from mallardduck import MallardDuck
from wildturkey import WildTurkey
from turkeyadapter import TurkeyAdapter

mduck = MallardDuck()
wturkey = WildTurkey()

turkeyadapt = TurkeyAdapter(wturkey)

mduck.quack()
mduck.fly()

wturkey.gobble()
wturkey.fly()

log.info("Turkey is adapted according to duck, so the below fly or quack will behave like duck")
turkeyadapt.quack()
turkeyadapt.fly()