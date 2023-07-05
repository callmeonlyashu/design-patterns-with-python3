from abstractClasses.CAbstractPizza import Pizza
from config.logger import logger as log
from AbstractFactoryPattern.CNYPizzaIngredientsFactory import NyPizzaIngredientFactory


class NYStyleVeggiePizza(Pizza):

    def __init__( self ):
        self.toppings = ["Cheese", "Mozarrela Cheese", "Veggies"]
        super().__init__()
        log.info("NY Style Veggie Pizza Creating...")
        self.factory = NyPizzaIngredientFactory()

    def prepare(self):
        log.info("Adding sauce")
        self.factory.createSauce()
        log.info("Tossing dough")
        self.factory.createDough()
        log.info("Adding toppings")
        self.factory.createToppings()
        log.info("Adding cheese")
        self.factory.createCheese()
        if self.toppings is not None:
            for topping in self.toppings:
                log.info("Added {} topping".format(topping))
