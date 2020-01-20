import tkinter as tk
import BaseDeDados as BD


class EcraAdicionarEmenta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.dia = tk.StringVar(self)
        self.tipo_eme = tk.StringVar(self)
        self.tipo_ref = tk.StringVar(self)
        self.lista_itens = tk.Listbox(self)
        self.lista_ids = tk.Listbox(self)
        self.itens_ementa = tk.Listbox(self)
        self.itens_ementa_ids = tk.Listbox(self)
        self.preco = tk.Entry(self)
        self.nome = tk.Entry(self)

        self.dias = []
        self.controller = controller

    def Mostrar(self, id):
        self.LimparEntradas()
        self.id_restaurante = id

        tk.Label(self, text="Nome da Ementa:").grid(row=0)
        self.nome.grid(row=0, column=1)
        self.nome.focus_set()

        tk.Label(self, text="Preco da Ementa:").grid(row=1)
        self.preco.grid(row=1, column=1)

        tk.Label(self, text="Escolher tipo de Refeição:").grid(row=2)
        tipos_refeicao = ['Pequeno-Almoço', 'Almoço', 'Jantar']
        self.tipo_ref.set(tipos_refeicao[0])
        opcao_tipo_refeicao = tk.OptionMenu(self, self.tipo_ref, *tipos_refeicao)
        opcao_tipo_refeicao.config(width=15)
        opcao_tipo_refeicao.grid(row=2, column=1)

        tk.Label(self, text="Escolher tipo de Ementa:").grid(row=3)
        tipos_ementa = ['Bebidas', 'Entradas', 'Pratos de Peixe', 'Pratos de Carne', 'Sobremesas']
        self.tipo_eme.set(tipos_ementa[0])
        opcao_tipo_ementa = tk.OptionMenu(self, self.tipo_eme, *tipos_ementa)
        opcao_tipo_ementa.config(width=15)
        opcao_tipo_ementa.grid(row=3, column=1)

        self.DiaSemana()
        tk.Label(self, text="Escolher Dia:").grid(row=4)
        self.dia.set(self.dias[0])
        opcao_dia = tk.OptionMenu(self, self.dia, *self.dias)
        opcao_dia.config(width=15)
        opcao_dia.grid(row=4, column=1)

        tk.Label(self, text="Escolher Itens:").grid(row=5)
        self.lista_itens.grid(row=6)

        itens = BD.SelecionarItens()
        for iten in itens:
            self.lista_ids.insert(tk.END, iten[0])
            self.lista_itens.insert(tk.END, iten[1])

        tk.Button(self, text="Adicionar Iten", command=self.AdicionarIten).grid(row=7)

        tk.Label(self, text="Itens Adicionados:").grid(row=0, column=3, padx=20)
        self.itens_ementa.grid(row=1, column=3, rowspan=20, padx=20, pady=0)

        tk.Button(self, text="Adicionar Ementa", command=self.VerificarEntradas).grid(row=9, column=1, pady=20)
        tk.Button(self, text="Voltar Atrás", command=self.VoltarAtras).grid(row=9, column=2, pady=20)

    def AdicionarIten(self):
        selection = self.lista_itens.curselection()
        if len(selection) == 0:
            return
        valor = self.lista_itens.get(selection[0])
        id_iten = self.lista_ids.get(selection[0])
        self.itens_ementa.insert(tk.END, valor)
        self.itens_ementa_ids.insert(tk.END, id_iten)

    def DiaSemana(self):
        import datetime
        for i in range(1, 8):
            dia_seguinte = datetime.datetime.now() + datetime.timedelta(days=i)
            self.dias.append(dia_seguinte.strftime('%d/%m/%Y'))

    def AdicionarEmenta(self):
        id_e = BD.InserirEmenta(self.id_restaurante, self.nome.get(), self.preco.get(), self.tipo_ref.get(),
                                self.tipo_eme.get(), self.dia.get())

        for id_iten in self.itens_ementa_ids.get(0, tk.END):
            BD.InserirItenEmenta(id_e, id_iten)

        self.VoltarAtras()

    def VerificarEntradas(self):
        if self.nome.get() == '' or len(self.nome.get()) > 15:
            return
        if not self.preco.get().isdigit():
            return
        if self.tipo_ref.get() == '':
            return
        if self.tipo_eme.get() == '':
            return
        if self.dia.get() == '':
            return
        if self.itens_ementa_ids.size() < 1:
            return
        self.AdicionarEmenta()

    def LimparEntradas(self):
        self.nome.delete(0, 'end')
        self.preco.delete(0, 'end')
        self.itens_ementa_ids.delete(0, tk.END)
        self.itens_ementa.delete(0, tk.END)

    def VoltarAtras(self):
        import EcraEmentas
        self.controller.MostrarFrame(EcraEmentas.EcraEmentas, self.id_restaurante)
