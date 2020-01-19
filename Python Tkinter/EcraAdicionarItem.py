import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarItem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lista_alergias = tk.Listbox(self)
        self.lista_alergias_ids = tk.Listbox(self)
        self.lista_dsgn = tk.Listbox(self)
        self.lista_ids = tk.Listbox(self)
        self.controller = controller

    def Mostrar(self, arg):
        tk.Label(self, text="Designação do Item").grid(row=0)
        tk.Label(self, text="Alergia").grid(row=1)

        self.dsgn = tk.Entry(self)
        self.dsgn.grid(row=0, column=1)
        self.dsgn.focus_set()


        tk.Label(self, text="Escolher Alergias").grid(row=2)
        self.lista_dsgn.grid(row=3)
        tk.Label(self, text="Alergias Adicionadas:").grid(row=2, column=3, padx=20)
        self.lista_alergias.grid(row=3, column=3, rowspan=20, padx=20, pady=0)

        alergias = BD.SelectAlergias()
        for alergia in alergias:
            self.lista_ids.insert(tk.END, alergia[0])
            self.lista_dsgn.insert(tk.END, alergia[1])

        tk.Button(self, text="Adicionar Item", command=self.VerificarEntradas).grid(row=5, column=1, pady=5)
        tk.Button(self, text="Adicionar Alergia", command=self.AdicionarAlergia).grid(row=4, column=1, pady=5)
        tk.Button(self, text="Voltar Atrás", command=self.MudarEcra).grid(row=5, column=2, pady=5)

    def VerificarEntradas(self):
        if (len(self.dsgn.get()) <= 0 or self.dsgn.get().isdigit()):
            return
        BD.InserirItem(self.dsgn.get())

        self.MudarEcra()

    def AdicionarAlergia(self):
        selection = self.lista_dsgn.curselection()
        valor = self.lista_dsgn.get(selection[0])
        id = self.lista_ids.get(selection[0])
        print("ID:" + str(id) + "VALOR" + valor)
        self.lista_alergias.insert(tk.END, valor)
        self.lista_alergias_ids.insert(tk.END, id)

    def MudarEcra(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)