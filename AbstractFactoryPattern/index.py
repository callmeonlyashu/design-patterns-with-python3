from CChicagoPizzaStore import ChicagoPizzaFactory
from CNYPizzaStore import NyPizzaFactory

pizzaNYCheese = NyPizzaFactory()
pizzaNYCheese.orderPizza('Veggie')

print("----------------------------------------------------------")

pizzaNYCheese = ChicagoPizzaFactory()
pizzaNYCheese.orderPizza('Clam')