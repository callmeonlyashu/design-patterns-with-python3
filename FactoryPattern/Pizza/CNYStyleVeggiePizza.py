from abstractClasses.CAbstractPizza import Pizza

class NYStyleVeggiePizza(Pizza):

    def __init__( self ):
        super().__init__()
        print("NY Style Veggie Pizza Creating...")