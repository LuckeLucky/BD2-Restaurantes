import tkinter as tk
from tkinter import ttk
import BaseDeDados as BD

class EcraEmentas(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        new_element_header=['1st','2nd','3rd','4th']
        self.tree = ttk.Treeview(self,columns=new_element_header, show="headings")
        self.tree.heading("1st", text="Designacao")
        self.tree.heading("2nd", text="Tipo Ementa")
        self.tree.heading("3rd", text="Tipo Refeição")
        self.tree.heading("4th", text="Preço")
        

        tk.Button(self, text = "Adicionar Ementa",command=self.IrParaAdicionarEmenta).pack(side=tk.TOP)

        #self.tree.bind("<Double-1>", self.DuploClique)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)


    def Mostrar(self,id):

        ementas = BD.SelectEmentasRestaurante(id)

        for ementa in ementas:
            self.tree.insert("" , "end",text=ementa[0], values=(ementa[1],ementa[2],ementa[3],ementa[4]))

    def IrParaAdicionarEmenta(self):
        
        import EcraCriarEmenta
        self.controller.MostrarFrame(EcraCriarEmenta.EcraCriarEmenta)