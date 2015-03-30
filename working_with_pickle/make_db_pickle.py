import pickle
from initdata import db

dbfilename = '../people-pickle'

def storeDbase(db=db, dbfilename=dbfilename):
    dbfile = open(dbfilename, 'wb')
    pickle.dump(db, dbfile)
    dbfile.close()

def loadDbase(dbfilename=dbfilename):
    dbfile = open(dbfilename, 'rb')
    db = pickle.load(dbfile)
    dbfile.close()
    return db

if __name__ == '__main__':
    storeDbase()
