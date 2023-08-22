import tkinter as tk
from tkinter import ttk

# Crie a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Defina o estilo dos botões
estilo_botoes = ttk.Style()
estilo_botoes.configure("Estilo.TButton", font=("Helvetica", 16))

# Crie o campo de entrada
entrada = ttk.Entry(janela, font=("Helvetica", 20), justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Função para inserir números e operadores no campo de entrada
def inserir_texto(valor):
    entrada.insert("end", valor)

# Função para limpar o campo de entrada
def limpar():
    entrada.delete(0, "end")

# Função para calcular
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, "end")
        entrada.insert("end", resultado)
    except:
        entrada.delete(0, "end")
        entrada.insert("end", "Erro")

# Crie os botões de números e operadores
botoes = [
    '1', '2', '3', '/',
    '4', '5', '6', '*',
    '7', '8', '9', '-',
    '0', 'C', '='
]

linha = 1
coluna = 0
for texto in botoes:
    if texto == '0':
        ttk.Button(janela, text=texto, style="Estilo.TButton", command=lambda num=texto: inserir_texto(num)).grid(row=linha, column=coluna, columnspan=2, padx=5, pady=5)
        coluna += 2
    elif texto == '=' or texto == 'C':
        ttk.Button(janela, text=texto, style="Estilo.TButton", command=calcular if texto == '=' else limpar).grid(row=linha, column=coluna, padx=5, pady=5)
        coluna += 1
    else:
        ttk.Button(janela, text=texto, style="Estilo.TButton", command=lambda num=texto: inserir_texto(num)).grid(row=linha, column=coluna, padx=5, pady=5)
        coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Inicie a interface gráfica
janela.mainloop()
