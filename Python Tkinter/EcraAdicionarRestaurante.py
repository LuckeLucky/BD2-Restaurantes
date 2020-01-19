import tkinter as tk
import BaseDeDados as bd


class EcraAdicionarRestaurante(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lista_lugares = tk.Listbox(self)
        self.tipo_l = tk.StringVar(self)
        self.morada = tk.Entry(self)
        self.telefone = tk.Entry(self)
        self.email = tk.Entry(self)
        self.nome = tk.Entry(self)
        self.lugares = tk.Entry(self)

        self.controller = controller

    def Mostrar(self, arg):

        tk.Label(self, text="Nome:").grid(row=0)
        tk.Label(self, text="Email:").grid(row=1)
        tk.Label(self, text="Telefone:").grid(row=2)
        tk.Label(self, text="Morada:").grid(row=3)

        self.nome.grid(row=0, column=1)
        self.nome.focus_set()
        self.email.grid(row=1, column=1)
        self.telefone.grid(row=2, column=1)
        self.morada.grid(row=3, column=1)

        tk.Label(self, text="Local:").grid(row=5, column=0)
        tipos_locais = ['Mesa', 'Balcão']
        self.tipo_l.set(tipos_locais[0])
        opcao_tipo_locais = tk.OptionMenu(self, self.tipo_l, *tipos_locais)
        opcao_tipo_locais.config(width=20)
        opcao_tipo_locais.grid(row=5, column=1)
        tk.Label(self, text="Lugares:").grid(row=6, column=0)
        self.lugares.grid(row=6, column=1)

        tk.Label(self, text="Locais Adicionados:").grid(row=0, column=4, padx=20)
        self.lista_lugares.grid(row=1, column=4, rowspan=8, padx=20)

        tk.Button(self, text="Adicionar Local", command=self.AdicionarLocal).grid(row=7, column=1, pady=5)
        tk.Button(self, text="Adicionar Restaurante", command=self.VerificarEntradas).grid(row=9, column=1, pady=20)
        tk.Button(self, text="Voltar Atrás", command=self.MudarEcra).grid(row=9, column=2, pady=20)

    def VerificarEntradas(self):
        if self.nome.get() == '' or len(self.nome.get()) > 20:
            return
        if (self.email.get() == '') or not ('@' in self.email.get()) or len(self.email.get()) > 50:
            return
        if len(self.telefone.get()) != 9 or not (self.telefone.get().isdigit()):
            return
        if self.morada.get() == '' or len(self.morada.get()) > 50:
            return

        self.AdicionarRestaurante()
        self.MudarEcra()

    def AdicionarLocal(self):
        n_lugares = self.lugares.get()
        if self.tipo_l.get() == "Mesa" and not n_lugares:
            return

        if self.tipo_l.get() == "Balcão":
            n_lugares = 1

        self.lista_lugares.insert(tk.END, self.tipo_l.get() + " lugares " + str(n_lugares))

    def AdicionarRestaurante(self):
        id_r = bd.InserirRestaurante(self.nome.get(), self.email.get(), self.telefone.get(), self.morada.get())
        for lugar in self.lista_lugares.get(0, tk.END):
            split_lugar = lugar.split()
            bd.InserirLocalConsumo(id_r, split_lugar[0], split_lugar[2])

    def LimparEntradas(self):
        self.nome.delete(0, 'end')
        self.email.delete(0, 'end')
        self.telefone.delete(0, 'end')
        self.morada.delete(0, 'end')
        self.lugares.delete(0, 'end')
        self.lista_lugares.delete(0, tk.END)

    def MudarEcra(self):
        self.LimparEntradas()
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)
