from abstractClasses.CAbstractBevarages import Bevarages

class Condiments(Bevarages):

    def __init__(self):
        super().__init__()

    """
    Abstract Functions that we need to extend in the sub-classes.
    """
    def description(self):
        pass

    def price(self):
        pass