from tkinter import mainloop
from tkinter.messagebox import showinfo
from kinter import MyGUI

class CustomGUI(MyGUI):
    def reply(self):
        showinfo(title='Popup', message='Ouch!')

if __name__ == '__main__':
    CustomGUI().pack()
    mainloop()
