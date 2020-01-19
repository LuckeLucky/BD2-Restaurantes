import tkinter as tk
from tkinter import ttk
import BaseDeDados as BD


class EcraEmentas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        botoes = tk.Frame(self)
        botoes.pack(side=tk.TOP)

        new_element_header = ['1st', '2nd', '3rd', '4th', '5th']
        self.tree = ttk.Treeview(self, columns=new_element_header, show="headings")
        self.tree.heading("1st", text="Designacao")
        self.tree.heading("2nd", text="Tipo Ementa")
        self.tree.heading("3rd", text="Tipo Refeição")
        self.tree.heading("4th", text="Data")
        self.tree.column("4th",width=110)
        self.tree.heading("5th", text="Preço")
        self.tree.column("5th",width=100)

        tk.Button(self, text="Adicionar Ementa", command=self.IrParaAdicionarEmenta).pack(in_=botoes, side=tk.LEFT)
        tk.Button(self, text="Voltar Atrás", command=self.VoltarAtras).pack(in_=botoes, side=tk.LEFT)

        # self.tree.bind("<Double-1>", self.DuploClique)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)

    def Mostrar(self, id):
        self.tree.delete(*self.tree.get_children())
        self.id_restaurante = id

        ementas = BD.SelectEmentasRestaurante(id)

        for ementa in ementas:
            self.tree.insert("", "end", text=ementa[0], values=(ementa[1], ementa[2], ementa[3], ementa[4], ementa[5]))

    def IrParaAdicionarEmenta(self):
        import EcraAdicionarEmenta
        self.controller.MostrarFrame(EcraAdicionarEmenta.EcraAdicionarEmenta, self.id_restaurante)

    def VoltarAtras(self):
        import EcraRestaurante
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante, self.id_restaurante)
