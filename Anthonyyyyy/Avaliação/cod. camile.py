import tkinter as tk
import math

janela = tk.Tk()
janela.title("Calculadora")

entrada = tk.Entry(janela, width=20, font=('Arial', 18), bd=5, justify='right')
entrada.grid(row=0, column=0, columnspan=4)

# Função para adicionar números e operadores
def clicar(valor):
    entrada.insert(tk.END, valor)

# Função para calcular o resultado
def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, tk.END)

# Função para calcular a raiz quadrada
def raiz():
    try:
        valor = float(entrada.get())
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para calcular porcentagem
def porcentagem():
    try:
        valor = float(entrada.get())
        resultado = valor / 100
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Botões
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('√', 5, 1), ('%', 5, 2)
]

for (texto, linha, coluna) in botoes:
    if texto == '=':
        tk.Button(janela, text=texto, width=5, height=2, command=calcular).grid(row=linha, column=coluna)
    elif texto == 'C':
        tk.Button(janela, text=texto, width=5, height=2, command=limpar).grid(row=linha, column=coluna)
    elif texto == '√':
        tk.Button(janela, text=texto, width=5, height=2, command=raiz).grid(row=linha, column=coluna)
    elif texto == '%':
        tk.Button(janela, text=texto, width=5, height=2, command=porcentagem).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna)

janela.mainloop()