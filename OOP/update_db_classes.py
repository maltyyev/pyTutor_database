import shelve
from OOP.make_db_classes import dbfilename

db = shelve.open(dbfilename)

sue = db['sue']
sue.raisePay(.1)
db['sue'] = sue

tom = db['tom']
tom.name = 'Thomas Edison'
db['tom'] = tom

db.close()
