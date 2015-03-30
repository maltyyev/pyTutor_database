import shelve
from OOP.person import Person
from OOP.manager import Manager

dbfilename = '../dbs/shelve-class.shlv'

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'dev')
    sue = Person('Sue Jones', 45, 40000, 'hdw')
    tom = Manager('Tom', 50, 50000)

    db = shelve.open(dbfilename)
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom
    db.close()
