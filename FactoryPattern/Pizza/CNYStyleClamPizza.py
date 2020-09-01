from abstractClasses.CAbstractPizza import Pizza

class NYStyleClamPizza(Pizza):

    def __init__( self ):
        super().__init__()
        print("NY Style Clam Pizza Creating...")