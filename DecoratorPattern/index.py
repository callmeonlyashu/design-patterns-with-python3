from CGeneralCoffee import GeneralCoffee
from CEpresso import Epresso
from CCappuccino import Cappuccino
from condiments.CLatte import Latte
from condiments.CMilk import Milk
from condiments.CMocha import Mocha
from config.logger import logger as log

beverages = Cappuccino()
beverages = Latte(beverages)
beverages = Milk(beverages)
beverages = Mocha(beverages)
# beverages = Mocha(beverages)

log.info( beverages.description() )
log.info( beverages.price() )