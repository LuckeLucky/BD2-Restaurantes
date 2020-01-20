import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarConsumo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.tipo_ref = tk.StringVar(self)
        self.tipo_eme = tk.StringVar(self)
        self.lista_ementas = tk.Listbox(self)
        self.local = tk.StringVar(self)
        self.cliente = tk.Entry(self)
        self.controller = controller
        self.locais_consumo = []

    def Mostrar(self, id):
        self.id_restaurante = id
        tk.Label(self, text="Cliente:").grid(row=0)
        self.cliente.grid(row=0, column=1)
        self.cliente.focus_set()

        self.LocaisConsumo()
        tk.Label(self, text="Local do Consumo:").grid(row=1)
        self.local.set(self.locais_consumo[0])
        opcao_local = tk.OptionMenu(self, self.local, *self.locais_consumo)
        opcao_local.config(width=15)
        opcao_local.grid(row=1, column=1)

        tk.Label(self, text="Tipo de Refeição:").grid(row=2)
        tipos_refeicao = ['Pequeno-Almoço', 'Almoço', 'Jantar']
        self.tipo_ref.set(tipos_refeicao[0])
        opcao_tipo_refeicao = tk.OptionMenu(self, self.tipo_ref, *tipos_refeicao)
        opcao_tipo_refeicao.config(width=15)
        opcao_tipo_refeicao.grid(row=2, column=1)

        tk.Label(self, text="Tipo de Ementa:").grid(row=3)
        tipos_ementa = ['Bebidas', 'Entradas', 'Pratos de Peixe', 'Pratos de Carne', 'Sobremesas']
        self.tipo_eme.set(tipos_ementa[0])
        opcao_tipo_ementa = tk.OptionMenu(self, self.tipo_eme, *tipos_ementa)
        opcao_tipo_ementa.config(width=15)
        opcao_tipo_ementa.grid(row=3, column=1)

        #self.Ementas()
        #tk.Label(self, text="Ementas:").grid(row=4)
        #self.lista_ementas.grid(row=5)

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

    def LocaisConsumo(self):
        locais_consumo = BD.SelecionarLocaisConsumoRestaurante(self.id_restaurante)
        for local_consumo in locais_consumo:
            self.locais_consumo.append(local_consumo[1] + " " + str(local_consumo[2]) + " lugares")

    def Ementas(self):
        ementas = BD.SelecionarEmentasDoDia(self.id_restaurante)
        for ementa in ementas:
            self.lista_ementas.insert(tk.END, ementa[0])

    def MudarEcra(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)
