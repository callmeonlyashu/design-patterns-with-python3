from abstractClasses.CAbstractPizza import Pizza

class NYStyleCheesePizza(Pizza):

    def __init__(self):
        super().__init__()
        print("NY Style Cheese Pizza Creating...")