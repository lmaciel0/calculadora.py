from tkinter import *

root = Tk()
root.title = ('Sua calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#A7A28F', font=('Lexend', 20, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)

# funções operadores


def botao_divisao():
    return


def botao_click():
    return


def botao_multriplica():
    return


divide = Button(root,
                text='+',
                padx=40,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('Lexend', 12, 'bold')
                )
divide.grid(row=0, column=4)

# primeira fileira
um = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: botao_click(1),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('Lexend', 12, 'bold')
            )
um.grid(row=1, column=1)

dois = Button(root,
              text='2',
              padx=40,
              pady=20,
              command=lambda: botao_click(2),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#320064',
              activebackground='#240046',
              relief=FLAT,
              font=('Lexend', 12, 'bold')
              )
dois.grid(row=1, column=2)

tres = Button(root,
              text='3',
              padx=40,
              pady=20,
              command=lambda: botao_click(3),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#320064',
              activebackground='#240046',
              relief=FLAT,
              font=('Lexend', 12, 'bold')
              )
tres.grid(row=1, column=3)

multiplica = Button(root,
                    text='x',
                    padx=40,
                    pady=20,
                    command=botao_multriplica,
                    fg='#FFFFFF',
                    activeforeground='#FFFFFF',
                    bg='#320064',
                    activebackground='#240046',
                    relief=FLAT,
                    font=('Lexend', 12, 'bold')
                    )
multiplica.grid(row=1, column=4)

root.mainloop()
