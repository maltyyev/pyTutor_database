import shelve
from shelves.make_db_shelve import dbfilename

db = shelve.open(dbfilename)
for key in db:
    print(key, '=>\n ', db[key])
print(db['sue']['name'])
db.close()
