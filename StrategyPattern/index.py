from CRealDuck import CRealDuck
from CRubberDuck import CRubberDuck
from CWoodenDuck import CWoodenDuck
from CMallokDuck import CMallokDuck
from config.logger import logger as log


objDuck = CRealDuck()
objDuck.display()
objDuck.getFlyBehaviour()
objDuck.getQuackBehaviour()

print('------------------------------------------')

objWDuck = CWoodenDuck()
objWDuck.display()
objWDuck.getFlyBehaviour()
objWDuck.getQuackBehaviour()

print('-------------------------------------------')

objRDuck = CRubberDuck()
objRDuck.display()
objRDuck.getFlyBehaviour()
objRDuck.getQuackBehaviour()


print('-------------------------------------------')

objRDuck = CMallokDuck()
objRDuck.display()
objRDuck.getFlyBehaviour()
objRDuck.getQuackBehaviour()