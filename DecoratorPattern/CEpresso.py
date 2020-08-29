from abstractClasses.CAbstractBevarages import Bevarages

class Epresso( Bevarages ):

    def __init__(self):
        super().__init__()

    def description(self):
        return "Epresso"

    def price(self):
        return 60
