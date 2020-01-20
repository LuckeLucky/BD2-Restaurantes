import tkinter as tk
import BaseDeDados as bd


class EcraEditarRestaurante(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.morada = tk.Entry(self)
        self.telefone = tk.Entry(self)
        self.email = tk.Entry(self)
        self.nome = tk.Entry(self)

        self.controller = controller

    def Mostrar(self, id):
        self.LimparEntradas()
        self.id_restaurante = id
        restaurante = bd.SelecionarRestaurante(id)

        tk.Label(self, text="Nome:").grid(row=0)
        tk.Label(self, text="Email:").grid(row=1)
        tk.Label(self, text="Telefone:").grid(row=2)
        tk.Label(self, text="Morada:").grid(row=3)

        self.nome.grid(row=0, column=1)
        self.nome.focus_set()
        self.email.grid(row=1, column=1)
        self.telefone.grid(row=2, column=1)
        self.morada.grid(row=3, column=1)

        for r in restaurante:
            self.nome.insert(0, r[1])
            self.email.insert(0, r[2])
            self.telefone.insert(0, r[3])
            self.morada.insert(0, r[4])

        tk.Button(self, text="Guardar Alterações", command=self.VerificarEntradas).grid(row=9, column=1, pady=20)
        tk.Button(self, text="Voltar Atrás", command=self.MudarEcra).grid(row=9, column=2, pady=20)
        tk.Button(self, text="Apagar Restaurante", command=self.ApagarRestaurante).grid(row=9, column=3, pady=20)

    def VerificarEntradas(self):
        if self.nome.get() == '' or len(self.nome.get()) > 20:
            return
        if (self.email.get() == '') or not ('@' in self.email.get()) or len(self.email.get()) > 50:
            return
        if len(self.telefone.get()) != 9 or not (self.telefone.get().isdigit()):
            return
        if self.morada.get() == '' or len(self.morada.get()) > 50:
            return

        self.AlterarRestaurante()
        self.MudarEcra()

    def AlterarRestaurante(self):
        bd.AlterarRestaurante(self.id_restaurante, self.nome.get(), self.email.get(), self.telefone.get(),
                              self.morada.get())

    def LimparEntradas(self):
        self.nome.delete(0, 'end')
        self.email.delete(0, 'end')
        self.telefone.delete(0, 'end')
        self.morada.delete(0, 'end')

    def MudarEcra(self):
        import EcraRestaurante
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante,self.id_restaurante)

    def ApagarRestaurante(self):
        bd.ApagarRestaurante(self.id_restaurante)
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)