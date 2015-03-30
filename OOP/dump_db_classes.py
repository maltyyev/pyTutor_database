import shelve
from OOP.make_db_classes import dbfilename

db = shelve.open(dbfilename)
for key in db:
    print(key, '=>\n ', db[key].job.capitalize(), db[key].name, db[key].pay)
