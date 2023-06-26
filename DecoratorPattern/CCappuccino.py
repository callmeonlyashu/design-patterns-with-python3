from abstractClasses.CAbstractBevarages import Bevarages

class Cappuccino( Bevarages ):

    def __init__(self):
        super().__init__()

    def description(self):

        return "Cappuccinno"

    def price(self):
        return 80
