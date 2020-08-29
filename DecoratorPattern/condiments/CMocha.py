from abstractClasses.CAbstractCondiments import Condiments

class Mocha( Condiments ):
  
    def __init__(self, bevarageObject):
        super().__init__()
        self.parentDescription = bevarageObject.description()
        self.parentPrice = bevarageObject.price()

    def description(self):
        return self.parentDescription + " ,Mocha"

    def price(self):
        return self.parentPrice + 15