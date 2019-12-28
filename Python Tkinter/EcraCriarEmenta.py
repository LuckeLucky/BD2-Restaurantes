import tkinter as tk
import BaseDeDados as BD

class EcraCriarEmenta(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        #Tipo de refeição
        tipo_ref = tk.StringVar(self)
        escolhas_refeicao = { 'Pequeno-almoço','Almoço','Jantar'}
        tipo_ref.set('Almoço') # Opção default
        popupMenu1 = tk.OptionMenu(self, tipo_ref, *escolhas_refeicao)
        tiporefeicao = tk.Label(self, text="Escolha o tipo de refeição")
        tiporefeicao.place(x = 15, y = 15)
        popupMenu1.place(x = 15, y = 45)

        #Tipo de ementa
        tipo_eme = tk.StringVar(self)
        escolhas_ementa = { 'Bebidas','Entradas','Pratos de Carne', 'Pratos de Peixe', 'Sobremesas'}
        tipo_eme.set('Bebidas') # Opção default
        popupMenu2 = tk.OptionMenu(self, tipo_eme, *escolhas_ementa)
        tipoementa = tk.Label(self, text="Escolha o tipo de ementa")
        tipoementa.place(x = 15, y = 90)
        popupMenu2.place(x = 15, y = 120)
        
        #Input para o nome da ementa
        nomeementa_text = tk.Label(text = "Nome da ementa:")
        nomeementa_text.place(x = 15, y = 160)
        nome_ementa = tk.StringVar()
        nomeementa_entry = tk.Entry(textvariable = nome_ementa, width = "30")
        nomeementa_entry.place(x = 15, y = 190)

        #Insert para DB

        self.close_button = tk.Button(self, text="Voltar atrás", )
        self.close_button.place( x=100, y = 280)
        self.close_button.config(width=10, height=3)

        self.close_button = tk.Button(self, text="Sair", )  
        self.close_button.place( x=200, y = 280)
        self.close_button.config(width=10, height=3)
