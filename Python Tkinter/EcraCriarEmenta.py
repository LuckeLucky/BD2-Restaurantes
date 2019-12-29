import tkinter as tk
import BaseDeDados as BD

class EcraCriarEmenta(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

    def Mostrar(self,id):
        self.id_restaurante=id

        tk.Label(self, text="Nome da Ementa:").grid(row=0)
        self.nome = tk.Entry(self)
        self.nome.grid(row=0, column=1)
        self.nome.focus_set()

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
        self.lista_itens= tk.Listbox(self)
        self.lista_ids=tk.Listbox(self)
        self.lista_itens.grid(row=5)

        itens =BD.SelectItens()
        for  iten in itens:
            self.lista_itens.insert(tk.END,iten[1])
            self.lista_ids.insert(tk.END,iten[0])
        
        tk.Button(self, text = "Adicionar Iten",command=self.AdicionarIten).grid(row=6)

        tk.Label(self, text="Itens Adicionados").grid(row=0,column=2)
        self.itens_ementa=tk.Listbox(self)
        self.itens_ementa.grid(row=1,column=2,rowspan=5)
        

    def AdicionarIten(self):
        selection=self.lista_itens.curselection()
        y= self.lista_itens.get(selection[0])
        x=self.lista_ids.get(selection[0])
        print ("ID:"+str(x)+"VALOR"+str(y))
        self.itens_ementa.insert(tk.END,str(y))
            

