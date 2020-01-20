from EcraInicial import *
from EcraRestaurante import *
from EcraEmentas import *
from EcraAdicionarRestaurante import *
from EcraAdicionarEmenta import *
from EcraAdicionarConsumo import *
from EcraAdicionarItem import *
from EcraStock import *



class PlataformaGestao(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry("800x400")
        self.title("Plataforma de Gestão")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (EcraInicial, EcraRestaurante, EcraEmentas, EcraAdicionarRestaurante, EcraAdicionarEmenta,
                  EcraAdicionarConsumo,EcraAdicionarItem,EcraStock):
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.MostrarFrame(EcraInicial)

    def MostrarFrame(self, cont, arg=None):
        frame = self.frames[cont]

        frame.Mostrar(arg)
        frame.tkraise()


app = PlataformaGestao()
app.mainloop()
