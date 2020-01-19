import tkinter as tk
from tkinter import ttk
import BaseDeDados as bd


class EcraInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.ordenar = 'nome'
        self.sentido = 'asc'
        self.controller = controller

        colunas = ['1st', '2nd', '3rd', '4th']
        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.heading("1st", text="Nome")
        self.tree.heading("2nd", text="Email")
        self.tree.heading("3rd", text="Telefone")
        self.tree.heading("4th", text="Morada")

        self.tree.bind("<Double-1>", self.DuploCliqueTree)
        self.tree.bind("<Button-1>", self.CliqueTree)

        pesquisa = tk.Frame(self)
        pesquisa.pack(side=tk.TOP)
        tk.Label(self, text="Pesquisar restaurante:").pack(in_=pesquisa, side=tk.LEFT)
        self.pesquisa = tk.Entry(self)
        self.pesquisa.pack(in_=pesquisa, side=tk.LEFT)
        self.pesquisa.focus_set()
        self.pesquisa.bind("<Return>", self.PreencherTreeEventos)

        botoes = tk.Frame(self)
        botoes.pack(side=tk.TOP)
        tk.Button(self, text="Adicionar Restaurante", command=self.CliqueAdicionarRestaurante).pack(in_=botoes,
                                                                                                    side=tk.LEFT)
        tk.Button(self, text="Adicionar Itens", command=self.CliqueAdicionarItem).pack(in_=botoes, side=tk.LEFT)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)

    def Mostrar(self, arg=None):
        self.pesquisa.delete(0, 'end')

        self.PreencherTreeInicial()

    def DuploCliqueTree(self, event):

        region = self.tree.identify("region", event.x, event.y)
        if region == "heading":
            return

        import EcraRestaurante
        item = self.tree.selection()[0]
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante, self.tree.item(item, "text"))

    def CliqueTree(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            return

        switch = {
            '#1': 'nome',
            '#2': 'email',
            '#3': 'telefone',
            '#4': 'morada'
        }
        if switch.get(self.tree.identify_column(event.x)) == self.ordenar:
            if self.sentido == "asc":
                self.sentido = "desc"
            else:
                self.sentido = "asc"
        else:
            self.ordenar = switch.get(self.tree.identify_column(event.x))
            self.sentido = "asc"

        self.PreencherTreeEventos(event)

    def Ordenar(self, event):
        self.PreencherTreeEventos(event)
        item = self.tree.getvar("text")
        print("you clicked on", self.tree.item(item, "text"))

    def CliqueAdicionarRestaurante(self):

        import EcraAdicionarRestaurante
        self.controller.MostrarFrame(EcraAdicionarRestaurante.EcraAdicionarRestaurante)

    def PreencherTreeInicial(self):
        self.tree.delete(*self.tree.get_children())
        restaurantes = bd.SelecionarRestaurantes(self.pesquisa.get(), self.ordenar, self.sentido)

        for index, restaurante in enumerate(restaurantes):
            self.tree.insert("", "end", text=restaurante[0],
                             values=(restaurante[1], restaurante[2], restaurante[3], restaurante[4]))

    def PreencherTreeEventos(self, event):
        self.tree.delete(*self.tree.get_children())
        restaurantes = bd.SelecionarRestaurantes(self.pesquisa.get(), self.ordenar, self.sentido)

        for index, restaurante in enumerate(restaurantes):
            self.tree.insert("", "end", text=restaurante[0],
                             values=(restaurante[1], restaurante[2], restaurante[3], restaurante[4]))

    def CliqueAdicionarItem(self):
        import EcraAdicionarItem
        self.controller.MostrarFrame(EcraAdicionarItem.EcraAdicionarItem)
