from tkinter import *

def botao_click(numero):
    global numero_1, numero_2
    numero_1 = numero_1 + str(numero)
    label_text.set(numero_1)

def botao_igual():
    global numero_1, numero_2
    numero_2 = label_text.get()
    result = int(numero_1) + int(numero_2)
    label_text.set(result)

def botao_limpa():
    global numero_1, numero_2
    numero_1 = ""
    numero_2 = ""
    label_text.set("")

root = Tk()
root.title("Calculadora")
root.geometry("408x355")

numero_1 = ""
numero_2 = ""

label_text = Label(root, text="0", font=("Helvetica", 20))
label_text.grid(row=0, column=0, columnspan=4)

# Botões de números
um = Button(root, text="1", command=lambda: botao_click(1))
um.grid(row=1, column=0)
dois = Button(root, text="2", command=lambda: botao_click(2))
dois.grid(row=1, column=1)
tres = Button(root, text="3", command=lambda: botao_click(3))
tres.grid(row=1, column=2)

quatro = Button(root, text="4", command=lambda: botao_click(4))
quatro.grid(row=2, column=0)
cinco = Button(root, text="5", command=lambda: botao_click(5))
cinco.grid(row=2, column=1)
seis = Button(root, text="6", command=lambda: botao_click(6))
seis.grid(row=2, column=2)

sete = Button(root, text="7", command=lambda: botao_click(7))
sete.grid(row=3, column=0)
oito = Button(root, text="8", command=lambda: botao_click(8))
oito.grid(row=3, column=1)
nove = Button(root, text="9", command=lambda: botao_click(9))
nove.grid(row=3, column=2)

zero = Button(root, text="0", command=lambda: botao_click(0))
zero.grid(row=4, column=0)

limpa = Button(root, text="C", command=botao_limpa)
limpa.grid(row=4, column=1)

igual = Button(root, text="=", command=botao_igual)
igual.grid(row=4, column=2)

root.mainloop()
