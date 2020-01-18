import tkinter as tk
from tkinter import ttk
import BaseDeDados as bd


class EcraInicial(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        colunas = ['1st', '2nd', '3rd', '4th']
        self.tree = ttk.Treeview(self, columns=colunas, show="headings")
        self.tree.heading("1st", text="Nome")
        self.tree.heading("2nd", text="Email")
        self.tree.heading("3rd", text="Telefone")
        self.tree.heading("4th", text="Morada")

        self.tree.bind("<Double-1>", self.DuploCliqueTree)

        pesquisa = tk.Frame(self)
        pesquisa.pack(side=tk.TOP)
        tk.Label(self, text="Pesquisar restaurante:").pack(in_=pesquisa, side=tk.LEFT)
        self.pesquisa = tk.Entry(self)
        self.pesquisa.pack(in_=pesquisa, side=tk.LEFT)
        self.pesquisa.focus_set()
        self.pesquisa.bind("<Return>", self.Pesquisar)

        botoes = tk.Frame(self)
        botoes.pack(side=tk.TOP)
        tk.Button(self, text="Adicionar Restaurante", command=self.CliqueAdicionarRestaurante).pack(in_=botoes, side=tk.LEFT)
        tk.Button(self, text="Adicionar Itens", command=self.CliqueAdicionarRestaurante).pack(in_=botoes, side=tk.LEFT)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)

    def Mostrar(self, arg=None):

        self.tree.delete(*self.tree.get_children())
        self.pesquisa.delete(0, 'end')
        restaurantes = bd.SelectRestaurantes()

        for index, restaurante in enumerate(restaurantes):
            self.tree.insert("", "end", text=restaurante[0], values=(restaurante[1], restaurante[2], restaurante[3], restaurante[4]))

    def DuploCliqueTree(self, event):

        import EcraRestaurante
        item = self.tree.selection()[0]
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante, self.tree.item(item, "text"))

    def CliqueAdicionarRestaurante(self):

        import EcraAdicionarRestaurante
        self.controller.MostrarFrame(EcraAdicionarRestaurante.EcraAdicionarRestaurante)

    def Pesquisar(self, event):

        self.tree.delete(*self.tree.get_children())
        restaurantes = bd.SearchRestaurante(self.pesquisa.get())

        for index, restaurante in enumerate(restaurantes):
            self.tree.insert("", "end", text=restaurante[0], values=(restaurante[1], restaurante[2], restaurante[3], restaurante[4]))