from tkinter import Tk, Label, Button, StringVar
from datetime import datetime, date, time

class DataHoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exibidor de Data e Hora")
        self.root.geometry("400x300")
        
        # Variáveis para armazenar os textos
        self.agora_var = StringVar()
        self.hoje_var = StringVar()
        self.data_escolhida_var = StringVar()
        self.hora_escolhida_var = StringVar()
        
        # Configuração dos rótulos e botões
        Label(root, text="Data e Hora Atuais:", font=('Arial', 12, 'bold')).pack(pady=5)
        Label(root, textvariable=self.agora_var).pack()
        
        Label(root, text="Data Atual:", font=('Arial', 12, 'bold')).pack(pady=5)
        Label(root, textvariable=self.hoje_var).pack()
        
        Label(root, text="Data Específica:", font=('Arial', 12, 'bold')).pack(pady=5)
        Label(root, textvariable=self.data_escolhida_var).pack()
        
        Label(root, text="Hora Específica:", font=('Arial', 12, 'bold')).pack(pady=5)
        Label(root, textvariable=self.hora_escolhida_var).pack()
        
        Button(root, text="Atualizar Datas", command=self.atualizar_datas).pack(pady=20)
        
        # Atualiza os valores inicialmente
        self.atualizar_datas()
    
    def atualizar_datas(self):
        # Data e hora atuais
        agora = datetime.now()
        self.agora_var.set(agora.strftime("%d/%m/%Y %H:%M:%S"))
        
        # Data atual
        hoje = date.today()
        self.hoje_var.set(hoje.strftime("%d/%m/%Y"))
        
        # Data específica
        data_exemplo = date(2024, 3, 7)
        self.data_escolhida_var.set(data_exemplo.strftime("%d/%m/%Y"))
        
        # Hora específica
        hora_exemplo = time(14, 35, 50)
        self.hora_escolhida_var.set(hora_exemplo.strftime("%H:%M:%S"))

# Criar e executar a aplicação
root = Tk()
app = DataHoraApp(root)
root.mainloop()