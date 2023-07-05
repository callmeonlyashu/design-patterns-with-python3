from abc import ABC, abstractmethod


class PizzaStore(ABC):

    def __init__(self):
        super().__init__()

    def orderPizza(self, store):
        pizza = self.createPizza(store)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    """
    Abstract Functions that we need to extend in the sub-classes.
    """
    @abstractmethod
    def createPizza(self, typeOfPizza):
        pass