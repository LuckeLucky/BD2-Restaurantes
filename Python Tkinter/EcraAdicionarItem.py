import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarItem(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.lista_alergias= tk.Listbox(self)
        self.nova = tk.Entry(self)
        self.alergia = tk.StringVar(self)
        self.dsgn = tk.Entry(self)
        self.controller = controller
        self.alergias = []

    def Mostrar(self, arg):
        self.LimparEntradas()
        tk.Label(self, text="Designação do Item").grid(row=0)
        self.dsgn.grid(row=0, column=1)
        self.dsgn.focus_set()

        self.Alergias()
        tk.Label(self, text="Alergias Possiveis:").grid(row=1)
        self.alergia.set(self.alergias[0])
        opcao_alergia = tk.OptionMenu(self, self.alergia, *self.alergias)
        opcao_alergia.config(width=20)
        opcao_alergia.grid(row=1, column=1)
        tk.Button(self, text="Adicionar Alergia", command=self.AdicionarAlergia).grid(row=1, column=2, pady=5)

        tk.Label(self, text="Nova Alergia?").grid(row=2)
        self.nova.grid(row=2, column=1)
        tk.Button(self, text="Adicionar Nova", command=self.AdicionarNovaAlergia).grid(row=2, column=2, pady=5)

        tk.Label(self,text="Alergias Adicionadas:").grid(row=0,column=3,padx=50)
        self.lista_alergias.grid(row=1,column=3,padx=50,rowspan=20)

        tk.Button(self, text="Adicionar Item", command=self.VerificarEntradas).grid(row=5, column=1, pady=5)
        tk.Button(self, text="Voltar Atrás", command=self.MudarEcra).grid(row=5, column=2, pady=5)

    def VerificarEntradas(self):
        if len(self.dsgn.get()) <= 0 or self.dsgn.get().isdigit():
            return

        self.Inserir()
        self.MudarEcra()

    def AdicionarAlergia(self):
        self.lista_alergias.insert(tk.END,self.alergia.get())

    def Alergias(self):
        alergias = BD.SelecionarAlergias()
        for alergia in alergias:
            self.alergias.append(alergia[0])

    def AdicionarNovaAlergia(self):
        if len(self.nova.get()) <= 0:
            return
        BD.InserirAlergia(self.nova.get())
        self.alergias.clear()
        self.nova.delete(0, 'end')
        self.Alergias()

    def Inserir(self):
        id_iten = BD.InserirIten(self.dsgn.get())
        for alergia in self.lista_alergias.get(0, tk.END):
            BD.InserirAlergiaIten(id_iten, alergia)

    def LimparEntradas(self):
        self.dsgn.delete(0, 'end')
        self.nova.delete(0, 'end')
        self.lista_alergias.delete(0, 'end')
        self.alergias.clear()
    def MudarEcra(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)
