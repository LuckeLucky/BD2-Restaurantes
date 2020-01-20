import tkinter as tk
import BaseDeDados as BD


class EcraStock(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.quantidade = tk.Label(self, text="Quantidade:")
        self.lista_itens = tk.Listbox(self, width=50)
        self.lista_ids = tk.Listbox(self)
        self.controller = controller
        self.quantidade_atual = 0

    def Mostrar(self, id):
        self.LimparEntradas()
        self.id_restaurante = id

        tk.Label(self, text="Itens em stock:").grid(row=0)
        self.lista_itens.grid(row=1,padx=20)
        tk.Button(self, text="+", command=self.Aumentar).grid(row=2)
        tk.Button(self, text="-", command=self.Diminuir).grid(row=3)
        self.quantidade.grid(row=4)

        self.lista_itens.bind("<<ListboxSelect>>", self.AcederIten)
        tk.Button(self, text="Guardar Alterações", command=self.Guardar).grid(row=5)
        tk.Button(self, text="Voltar Atrás", command=self.VoltarAtras).grid(row=6)

        self.PreencherListBox()

    def PreencherListBox(self):
        itens = BD.SelecionarStockRestaurante(self.id_restaurante)
        for iten in itens:
            self.lista_ids.insert(tk.END, iten[0])
            self.lista_itens.insert(tk.END, str(iten[2]) + '-->' + iten[1])

    def Aumentar(self):
        self.quantidade_atual += 1
        self.quantidade.config(text="Quantidade:" + str(self.quantidade_atual))

    def Diminuir(self):
        if self.quantidade_atual==0:
            return
        self.quantidade_atual -= 1
        self.quantidade.config(text="Quantidade:" + str(self.quantidade_atual))

    def AcederIten(self, event):
        selection = self.lista_itens.curselection()
        if len(selection) == 0:
            return
        valor = self.lista_itens.get(selection[0])
        self.id_iten_actual = self.lista_ids.get(selection[0])
        split = valor.split("-->")
        self.quantidade.config(text="Quantidade:" + split[0])
        self.quantidade_atual = int(split[0])

    def Guardar(self):
        BD.AlterarStockIten(self.id_restaurante, self.id_iten_actual, self.quantidade_atual)
        self.LimparEntradas()
        self.PreencherListBox()

    def LimparEntradas(self):
        self.lista_ids.delete(0, tk.END)
        self.lista_itens.delete(0, tk.END)
        self.quantidade.config(text="Quantidade:")

    def VoltarAtras(self):
        import EcraRestaurante
        self.controller.MostrarFrame(EcraRestaurante.EcraRestaurante, self.id_restaurante)
