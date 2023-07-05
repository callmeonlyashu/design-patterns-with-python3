from abstractClasses.CAbstractPizzaStore import PizzaStore
from Pizza.CNYStyleCheesePizza import NYStyleCheesePizza
from Pizza.CNYStyleClamPizza import NYStyleClamPizza
from Pizza.CNYStyleVeggiePizza import NYStyleVeggiePizza
from config.logger import logger as log


class NyPizzaFactory(PizzaStore):
    
    def createPizza(self, type):
        if type == 'Cheese':
            return NYStyleCheesePizza()
        elif type == "Veggie":
            return NYStyleVeggiePizza()
        elif type == "Clam":
            return NYStyleClamPizza()
        else:
            return None
