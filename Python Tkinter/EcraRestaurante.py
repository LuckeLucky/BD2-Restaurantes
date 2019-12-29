import tkinter as tk
import BaseDeDados as BD

class EcraRestaurante(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

    def Mostrar(self,id):
        self.restaurante_id=id
        restaurante=BD.SelectRestaurante(id)

        butao_ementas = tk.Button(self, text="Ementas",command=self.IrParaEmentas, width=15, height = 2)
        butao_ementas.grid(row=5,column=2)

        butao_stock= tk.Button(self, text="Stock",command=self.IrParaEmentas, width=15, height = 2)
        butao_stock.grid(row=5,column=3)

        butao_consumos= tk.Button(self, text="Consumos",command=self.IrParaEmentas, width=15, height = 2)
        butao_consumos.grid(row=5,column=4)

        butao_voltar_atras = tk.Button(self, text="Voltar atrás",command=self.VoltarAtras, width=15, height = 2)
        butao_voltar_atras.grid(row=6,column=2)

        butao_editar = tk.Button(self, text="Editar",command=self.VoltarAtras, width=15, height = 2)
        butao_editar.grid(row=6,column=3)

        for r in restaurante:
            tk.Label(self, text="Nome:"+r[1]).grid(row=1,column=1,padx=10)
            tk.Label(self, text="Email:"+r[2]).grid(row=2,column=1,padx=10)
            tk.Label(self, text="Telefone:"+r[3]).grid(row=3,column=1,padx=10)
            tk.Label(self, text="Morada:"+r[4]).grid(row=4,column=1,padx=10)

    def VoltarAtras(self):
        import EcraInicial
        self.controller.MostrarFrame(EcraInicial.EcraInicial)
    
    def IrParaEmentas(self):
        import EcraEmentas
        self.controller.MostrarFrame(EcraEmentas.EcraEmentas,self.restaurante_id)



        

        
    