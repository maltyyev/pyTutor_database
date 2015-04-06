import shelve
from tkinter import *
from tkinter.messagebox import showerror
from OOP.person import Person

filename = 'dbs/shelve-class.shlv'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    form = Frame(window)
    form.pack()
    entries = {}

    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent

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

db = shelve.open(filename)
window = makeWidgets()
window.mainloop()
db.close()
