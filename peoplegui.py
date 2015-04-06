import shelve
from tkinter import *
from tkinter.messagebox import showerror
from OOP.person import Person

shelvename = 'dbs/shelve-class.shlv'
fieldnames = ('name', 'age', 'pay', 'job')

def makeWidgets():
    global entries
    window = Tk()
    form = Frame(window)
    form.pack()
    entries = {}
    for (i, field) in enumerate(('key',) + fieldnames):
        Label(form, text=field).grid(row=i, column=0)
        ent = Entry(form)
        ent.grid(row=i, column=1)
        entries[field] = ent
    Button(window, text='Fetch', command=fetch).pack(side=LEFT)
    Button(window, text='Update', command=update).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window

def fetch():
    key = entries['key'].get()
    try:
        record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))

def update():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        record = Person(name='?', age='?')

    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()
