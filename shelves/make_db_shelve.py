import shelve
from initdata import bob, sue, tom

dbfilename = '../dbs/people-shelve.shlv'

if __name__ == '__main__':
    db = shelve.open(dbfilename)
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()
