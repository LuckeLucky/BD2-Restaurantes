import tkinter as tk
from tkinter import ttk
import BaseDeDados as BD

class EcraInicial(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        new_element_header=['1st','2nd','3rd','4th']
        self.tree = ttk.Treeview(self,columns=new_element_header, show="headings")
        self.tree.heading("1st", text="Nome")
        self.tree.heading("2nd", text="Email")
        self.tree.heading("3rd", text="Telefone")
        self.tree.heading("4th", text="Morada")
        
        self.ListarRestaurantes()

        tk.Label(self, text = "Adicionar Ementa").pack(side=tk.TOP)

        self.tree.bind("<Double-1>", self.DuploClique)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)


    def ListarRestaurantes(self):

        restaurantes = BD.SelectRestaurantes()

        for index,restaurante in enumerate(restaurantes):
            self.tree.insert("" , "end",text=restaurante[0], values=(restaurante[1],restaurante[2],restaurante[3],restaurante[4]))

    def DuploClique(self, event):

        import EcraRestaurante
        item = self.tree.selection()[0]
        print("you clicked on", self.tree.item(item,"text"))
        #limpar a arvore :) self.tree.delete(*self.tree.get_children())
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante,self.tree.item(item,"text"))
