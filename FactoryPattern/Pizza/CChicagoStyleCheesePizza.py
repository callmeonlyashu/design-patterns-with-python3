from abstractClasses.CAbstractPizza import Pizza

class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        print("Chicago Style Cheese Pizza Creating...")