from abstractClasses.CAbstractBevarages import Bevarages

class GeneralCoffee( Bevarages ):

    def __init__(self):
        super().__init__()

    def description(self):
        return "General Coffee"

    def price(self):
        return 50
