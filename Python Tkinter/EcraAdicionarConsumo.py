import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarConsumo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.nif=tk.Entry(self)
        self.preco = 0
        self.preco_total = tk.Label(self, text="Preço Total:0")
        self.ementas_consumidas = tk.Listbox(self, width=30)
        self.ementas_consumidas_ids = tk.Listbox(self)
        self.podecausar = tk.Label(self, text="")
        self.tipo_ref = tk.StringVar(self)
        self.tipo_eme = tk.StringVar(self)
        self.lista_ementas = tk.Listbox(self, width=30)
        self.ids_ementas = tk.Listbox(self)
        self.local = tk.StringVar(self)
        self.cliente = tk.Entry(self)
        self.controller = controller
        self.locais_consumo = []

    def Mostrar(self, id):
        self.LimparEntradas()
        self.id_restaurante = id
        tk.Label(self, text="Cliente:").grid(row=0)
        self.cliente.grid(row=0, column=1)
        self.cliente.focus_set()

        tk.Label(self, text="NIF:").grid(row=1)
        self.nif.grid(row=1,column=1)

        self.LocaisConsumo()
        tk.Label(self, text="Local do Consumo:").grid(row=2)
        self.local.set(self.locais_consumo[0])
        opcao_local = tk.OptionMenu(self, self.local, *self.locais_consumo)
        opcao_local.config(width=20)
        opcao_local.grid(row=2, column=1)

        tk.Label(self, text="Tipo de Refeição:").grid(row=3)
        tipos_refeicao = ['Pequeno-Almoço', 'Almoço', 'Jantar']
        self.tipo_ref.set(tipos_refeicao[0])
        opcao_tipo_refeicao = tk.OptionMenu(self, self.tipo_ref, *tipos_refeicao, command=self.Ementas)
        opcao_tipo_refeicao.config(width=20)
        opcao_tipo_refeicao.grid(row=3, column=1)

        tk.Label(self, text="Tipo de Ementa:").grid(row=4)
        tipos_ementa = ['Bebidas', 'Entradas', 'Pratos de Peixe', 'Pratos de Carne', 'Sobremesas']
        self.tipo_eme.set(tipos_ementa[0])
        opcao_tipo_ementa = tk.OptionMenu(self, self.tipo_eme, *tipos_ementa, command=self.Ementas)
        opcao_tipo_ementa.config(width=20)
        opcao_tipo_ementa.grid(row=4, column=1)

        self.Ementas("<ola>")
        tk.Label(self, text="Ementas:").grid(row=5)
        self.lista_ementas.grid(row=5, column=1)
        self.lista_ementas.bind("<<ListboxSelect>>", self.VerAlergiasEmenta)

        tk.Button(self, text="Adicionar Ementa", command=self.AdicionarAoConsumo).grid(row=6, column=1, padx=10)

        self.podecausar.grid(row=2, column=3, padx=30)

        tk.Label(self, text="Ementas Consumidas").grid(row=3, column=3)
        self.ementas_consumidas.grid(row=4, column=3, padx=30,rowspan=6)

        self.preco_total.grid(row=20, column=3, padx=30)

        tk.Button(self, text="Adicionar Consumo", command=self.VerificarEntradas).grid(row=20, column=1, pady=5)
        tk.Button(self, text="Voltar Atrás", command=self.RetirarAoConsumo).grid(row=20, column=2, pady=5)

    def LocaisConsumo(self):
        locais_consumo = BD.SelecionarLocaisConsumoRestaurante(self.id_restaurante)
        for local_consumo in locais_consumo:
            self.locais_consumo.append(local_consumo[1] + " " + str(local_consumo[2]) + " lugares")

    def Ementas(self, event):
        ementas = BD.SelecionarEmentasDisponiveis(self.id_restaurante, self.tipo_eme.get(), self.tipo_ref.get())
        for ementa in ementas:
            self.lista_ementas.insert(tk.END, ementa[1] + " Preço " + ementa[2])
            self.ids_ementas.insert(tk.END, ementa[0])

    def VerAlergiasEmenta(self, event):
        self.podecausar.config(text="")
        selection = self.lista_ementas.curselection()
        if len(selection) == 0:
            return
        alergias = BD.AlergiasEmenta(self.ids_ementas.get(selection[0]))
        if alergias == '':
            self.podecausar.config(text="Não Causa Alergias")
        else:
            self.podecausar.config(text="Pode Causar:" + alergias)

    def AdicionarAoConsumo(self):
        selection = self.lista_ementas.curselection()
        if len(selection) == 0:
            return
        possivel = BD.ConsumirEmenta(self.id_restaurante, self.ids_ementas.get(selection[0]))
        if possivel:
            self.ementas_consumidas.insert(tk.END, self.lista_ementas.get(selection[0]))
            self.ementas_consumidas_ids.insert(tk.END, self.ids_ementas.get(selection[0]))
            linha = self.lista_ementas.get(selection[0]).split("Preço", 2)
        else:
            return
        preco = linha[1].split(' €')
        preco = preco[0]
        preco = preco.replace(',', '.')
        self.preco += float(preco)
        self.preco_total.config(text="Preço Total:" + str(self.preco))

    def VerificarEntradas(self):
        if len(self.cliente.get()) <= 0 or len(self.cliente.get()) > 20:
            return
        if len(self.nif.get()) != 9 or not (self.nif.get().isdigit()):
            return
        if self.preco == 0:
            return
        self.InserirConsumo()
        self.MudarEcra()

    def InserirConsumo(self):
        local=self.local.get().split(" ")
        self.preco=str(self.preco)
        self.preco=self.preco.replace('.',',')
        id_consumo=BD.InserirConsumo(self.id_restaurante,self.cliente.get(),self.nif.get(),local[0], local[1],self.preco)

        for id_ementa in self.ementas_consumidas_ids.get(0, tk.END):
            BD.InserirConsumoEmenta(id_consumo, id_ementa)

    def RetirarAoConsumo(self):
        for id_ementa in self.ementas_consumidas_ids.get(0, tk.END):
            BD.DeConsumirEmenta(self.id_restaurante, id_ementa)

        self.MudarEcra()

    def LimparEntradas(self):
        self.cliente.delete(0, 'end')
        self.nif.delete(0, 'end')
        self.preco=0
        self.locais_consumo.clear()
        self.ementas_consumidas_ids.delete(0, 'end')
        self.ementas_consumidas.delete(0, 'end')
        self.lista_ementas.delete(0, tk.END)
        self.ids_ementas.delete(0, tk.END)
        self.podecausar.config(text="")

    def MudarEcra(self):
        import EcraRestaurante
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante, self.id_restaurante)
