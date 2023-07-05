from CDatabase import Database
from config.logger import logger as log


db = Database.getInstance()
log.info(db)
db1 = Database.getInstance()
log.info(db1)