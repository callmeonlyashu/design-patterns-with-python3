from abstractClasses.CAbstractCondiments import Condiments

class Latte( Condiments ):
  
    def __init__(self, bevarageObject):
        super().__init__()
        self.parentDescription = bevarageObject.description()
        self.parentPrice = bevarageObject.price()

    def description(self):
        return self.parentDescription + " ,Latte"

    def price(self):
        return self.parentPrice + 10