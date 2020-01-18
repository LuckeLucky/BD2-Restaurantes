import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarConsumo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

    def Mostrar(self, arg):
        tk.Label(self, text="Cliente").grid(row=0)
        tk.Label(self, text="Local do Consumo").grid(row=1)
        tk.Label(self, text="Valor do Consumo").grid(row=2)

        global local_c
        local_c = ["Interior - Mesas", "Interior - Balcão", "Exterior - Pátio"]
        l_consumo = tk.StringVar(self)
        l_consumo = tk.StringVar(self).set(local_c[0])

        self.cliente = tk.Entry(self)
        self.cliente.grid(row=0, column=1)
        self.cliente.focus_set()

        self.local_consumo = tk.Entry(self)
        self.local_consumo = tk.OptionMenu(self, l_consumo, *local_c, command=self.IDConsumo)
        self.local_consumo.config(width=20)
        self.local_consumo.grid(row=1, column=1)

        self.preco_total = tk.Entry(self)
        self.preco_total.grid(row=2, column=1)

        tk.Button(self, text="Adicionar", command=self.VerificarEntradas).grid(row=5, column=1, pady=5)
        tk.Button(self, text="Voltar Atrás", command=self.MudarEcra).grid(row=5, column=2, pady=5)

    def IDConsumo(self, value):
        global local_c
        global id_consumo
        id_consumo = local_c.index(value) + 1

    def VerificarEntradas(self):
        global id_consumo
        if (len(self.cliente.get()) <= 0 or not (self.cliente.get().isdigit())):
            return
        if (len(self.preco_total.get()) < 0 or not (self.preco_total.get().isdigit())):
            return
        BD.InsertConsumo(self.cliente.get(), id_consumo, self.preco_total.get())

        self.MudarEcra()

    def MudarEcra(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)