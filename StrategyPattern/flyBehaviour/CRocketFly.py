from abstractClasses.AbstractFlyBehaviour import FlyBehaviour


class CRocketFly(FlyBehaviour):

    def __init__(self):
        super().__init__()

    def fly(self):
        print("I can fly with a Rocket.")