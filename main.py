from tkinter import *

root = Tk()
root.title('Sua calculadora')
root.geometry('408x355')
root.minsize(408, 355)
root.maxsize(408, 355)

root.configure(background='#000000')  # Cor de fundo preta

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#444444', font=('Helvetica', 20, 'bold'), justify=CENTER)  # Fonte Helvetica
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


def botao_subtracao():
    return


def botao_adicao():
    return


def botao_limpa():
    return


def botao_igual():
    return


divide = Button(root,
                text='/',
                padx=43,
                pady=20,
                command=botao_divisao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#FF9500',
                activebackground='#E99600',
                relief=FLAT,
                font=('Helvetica', 12, 'bold')
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
            bg='#FF9500',
            activebackground='#E99600',
            relief=FLAT,
            font=('Helvetica', 12, 'bold')
            )
um.grid(row=1, column=1)

dois = Button(root,
              text='2',
              padx=40,
              pady=20,
              command=lambda: botao_click(2),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
dois.grid(row=1, column=2)

tres = Button(root,
              text='3',
              padx=40,
              pady=20,
              command=lambda: botao_click(3),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
tres.grid(row=1, column=3)

multiplica = Button(root,
                    text='x',
                    padx=40,
                    pady=20,
                    command=botao_multriplica,
                    fg='#FFFFFF',
                    activeforeground='#FFFFFF',
                    bg='#FF9500',
                    activebackground='#E99600',
                    relief=FLAT,
                    font=('Helvetica', 12, 'bold')
                    )
multiplica.grid(row=1, column=4)

# segunda fileira
quatro = Button(root,
                text='4',
                padx=40,
                pady=20,
                command=lambda: botao_click(4),
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#FF9500',
                activebackground='#E99600',
                relief=FLAT,
                font=('Helvetica', 12, 'bold')
                )
quatro.grid(row=2, column=1)

cinco = Button(root,
               text='5',
               padx=40,
               pady=20,
               command=lambda: botao_click(5),
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#FF9500',
               activebackground='#E99600',
               relief=FLAT,
               font=('Helvetica', 12, 'bold')
               )
cinco.grid(row=2, column=2)

seis = Button(root,
              text='6',
              padx=40,
              pady=20,
              command=lambda: botao_click(6),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
seis.grid(row=2, column=3)

menos = Button(root,
               text='-',
               padx=41.5,
               pady=20,
               command=botao_subtracao,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#FF9500',
               activebackground='#E99600',
               relief=FLAT,
               font=('Helvetica', 12, 'bold')
               )
menos.grid(row=2, column=4)

# terceira fileira
sete = Button(root,
              text='7',
              padx=40,
              pady=20,
              command=lambda: botao_click(7),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
sete.grid(row=3, column=1)

oito = Button(root,
              text='8',
              padx=40,
              pady=20,
              command=lambda: botao_click(8),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
oito.grid(row=3, column=2)

nove = Button(root,
              text='9',
              padx=40,
              pady=20,
              command=lambda: botao_click(9),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
nove.grid(row=3, column=3)

mais = Button(root,
              text='+',
              padx=40,
              pady=20,
              command=botao_adicao,
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 12, 'bold')
              )
mais.grid(row=3, column=4)

# quarta fileira
zero = Button(root,
              text='0',
              padx=93,
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activeforeground='#FFFFFF',
              bg='#FF9500',
              activebackground='#E99600',
              relief=FLAT,
              font=('Helvetica', 10, 'bold')
              )
zero.grid(row=4, column=1, columnspan=2)

limpa = Button(root,
               text='C',
               padx=41,
               pady=20,
               command=botao_limpa,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#FF9500',
               activebackground='#E99600',
               relief=FLAT,
               font=('Helvetica', 10, 'bold')
               )
limpa.grid(row=4, column=3)

igual = Button(root,
               text='=',
               padx=40,
               pady=20,
               command=botao_igual,
               fg='#FFFFFF',
               activeforeground='#FFFFFF',
               bg='#FF9500',
               activebackground='#E99600',
               relief=FLAT,
               font=('Helvetica', 10, 'bold')
               )
igual.grid(row=4, column=4)

root.mainloop()
