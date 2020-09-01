from abstractClasses.CAbstractPizzaStore import PizzaStore
from Pizza.CChicagoStyleCheesePizza import ChicagoStyleCheesePizza
from Pizza.CChicagoStyleClamPizza import ChicagoStyleClamPizza
from Pizza.CChicagoStyleVeggiePizza import ChicagoStyleVeggiePizza

class ChicagoPizzaFactory( PizzaStore ):
    
    def createPizza(self, type):
        if( type == 'Cheese' ):  
            return ChicagoStyleCheesePizza()
        elif( type == "Clam" ):
            return ChicagoStyleClamPizza()
        elif( type == "Veggie" ):
            return ChicagoStyleVeggiePizza()
        else:
            return None