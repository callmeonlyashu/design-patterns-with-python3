from abstractClasses.AbstractQuackBehaviour import QuackBehaviour


class CMallokQuack(QuackBehaviour):

    def __init__(self):
        super().__init__()

    def quack(self):
        print("I can speak like a Mallok Duck")