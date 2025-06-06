import tkinter as tk
from tkinter import messagebox

# Função que será executada quando o botão for clicado
def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão!")

# 1. Criar a janela principal (root window)
janela = tk.Tk()
janela.title("Exemplo de Botão")  # Define o título da janela
janela.geometry("300x150")       # Define o tamanho da janela (largura x altura)

# 2. Criar um botão
botao = tk.Button(
    janela,                     # Indica que o botão pertence à janela principal
    text="Clique aqui",         # Texto que aparece no botão
    command=mostrar_mensagem,   # Função a ser chamada quando clicado
    bg="lightblue",             # Cor de fundo do botão (background)
    fg="black",                 # Cor do texto (foreground)
    font=("Arial", 12),         # Fonte do texto
    width=15,                   # Largura do botão em caracteres
    height=2                    # Altura do botão em linhas de texto
)

# 3. Posicionar o botão na janela
botao.pack(pady=20)  # O pack() organiza o widget, pady adiciona espaço vertical

# 4. Iniciar o loop principal da aplicação
janela.mainloop()