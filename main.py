from tkinter import *

root = Tk()
root.title = ('Sua calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='a7a28f', font=('Lexend', 20, 'bold'), justify=CENTER)


root.mainloop()
