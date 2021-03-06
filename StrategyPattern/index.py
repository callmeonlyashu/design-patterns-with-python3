from CRealDuck import CRealDuck
from CRubberDuck import CRubberDuck
from CWoodenDuck import CWoodenDuck

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