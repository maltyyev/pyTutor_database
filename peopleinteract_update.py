import shelve
from OOP.person import Person

db = shelve.open('dbs/shelve-class.shlv')
fieldnames = ('name', 'age', 'job', 'pay')

while True:
    key = input('\nKey? => ')

    if not key: break
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')
    for field in fieldnames:
        currval = getattr(record, field)
        newtext = input('\t[%s]=%s\n\tnew? => ' % (field, currval))
        if newtext:
            setattr(record, field, newtext)
    db[key] = record

db.close()
