from CChicagoPizzaFactory import ChicagoPizzaFactory
from CNYPizzaFactory import NyPizzaFactory

pizzaNYCheese = NyPizzaFactory()
pizzaNYCheese.orderPizza('Veggie')

print("----------------------------------------------------------")

pizzaNYCheese = ChicagoPizzaFactory()
pizzaNYCheese.orderPizza('Clam')