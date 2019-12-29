import tkinter as tk
import BaseDeDados as BD

class EcraAdicionarRestaurante(tk.Frame):
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

    def Mostrar(self,arg):
        tk.Label(self, text="Nome").grid(row=0)
        tk.Label(self, text="Email").grid(row=1)
        tk.Label(self, text="Telefone").grid(row=2)
        tk.Label(self, text="Morada").grid(row=3)

        self.nome = tk.Entry(self)
        self.nome.grid(row=0, column=1)
        self.nome.focus_set()
        self.email = tk.Entry(self)
        self.email.grid(row=1, column=1)
        self.telefone = tk.Entry(self)
        self.telefone.grid(row=2, column=1)
        self.morada = tk.Entry(self)
        self.morada.grid(row=3, column=1)

        tk.Button(self, text = "Adicionar",command=self.VerificarEntradas).grid(row=5,column=1,pady=5)
        tk.Button(self, text = "Voltar Atrás",command=self.MudarEcra).grid(row=5,column=2,pady=5)

    def VerificarEntradas(self):
        if( self.nome.get()=='' or len(self.nome.get())>20):
            return
        if( (self.email.get()=='' ) or not('@' in self.email.get()) or len(self.email.get())>50):
            return
        if( len(self.telefone.get()) !=9 or not (self.telefone.get().isdigit())):
            return
        if( self.morada.get()=='' or len(self.morada.get())>50):
            return
        BD.InsertRestaurante(self.nome.get(),self.email.get(),self.telefone.get(),self.morada.get())

        self.MudarEcra()

    def MudarEcra(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)