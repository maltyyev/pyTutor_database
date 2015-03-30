import shelve
from shelves.make_db_shelve import dbfilename

db = shelve.open(dbfilename)

sue = db['sue']
sue['pay'] *= 1.10
db['sue'] = sue

tom = db['tom']
tom['name'] = 'Thomas Edison'
db['tom'] = tom

db.close()
