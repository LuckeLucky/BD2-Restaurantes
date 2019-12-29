import tkinter as tk
import BaseDeDados as BD

class EcraCriarEmenta(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

    def Mostrar(self,arg):

        tk.Label(self, text="Nome da Ementa:").grid(row=0)
        self.nome = tk.Entry(self)
        self.nome.grid(row=0, column=1)

        tk.Label(self, text="Preco da Ementa:").grid(row=1)
        self.preco = tk.Entry(self)
        self.preco.grid(row=1, column=1)

        tk.Label(self, text="Escolher tipo de Refeição:").grid(row=2)
        tipos_refeicao=['Pequeno-almoço','Almoço','Jantar']
        tipo_ref = tk.StringVar(self)
        tipo_ref.set(tipos_refeicao[0])
        opcao_tipo_refeicao=tk.OptionMenu(self, tipo_ref, *tipos_refeicao)
        opcao_tipo_refeicao.config(width=20)
        opcao_tipo_refeicao.grid(row=2,column=1)

        tk.Label(self, text="Escolher tipo de Ementa:").grid(row=3)
        tipos_ementa=['Bebida','Entrada','Prato de Carne', 'Prato de Peixe', 'Sobremesa']
        tipo_eme = tk.StringVar(self)
        tipo_eme.set(tipos_ementa[0])
        opcao_tipo_ementa=tk.OptionMenu(self, tipo_eme, *tipos_ementa)
        opcao_tipo_ementa.config(width=20)
        opcao_tipo_ementa.grid(row=3,column=1)

        tk.Label(self, text="Escolher Itens").grid(row=4)
        self.lista_itens.grid(row=5)

        itens =BD.SelectItens()
        


        

