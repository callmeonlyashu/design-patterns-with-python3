from CGeneralCoffee import GeneralCoffee
from CEpresso import Epresso
from CCappuccino import Cappuccino
from condiments.CLatte import Latte
from condiments.CMilk import Milk
from condiments.CMocha import Mocha

beverages = Cappuccino()
beverages = Latte(beverages)
beverages = Milk(beverages)
beverages = Mocha(beverages)
beverages = Mocha(beverages)

print( beverages.description() )
print( beverages.price() )