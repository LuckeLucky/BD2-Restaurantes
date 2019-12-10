from tkinter import *
import tkinter as tk
import os
import psycopg2
import restaurantes as Rt
import itens as It
import ementas as Et


class ecran_entrada(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Gestão de Restaurantes")

        self.geometry("600x400+30+30")

        self.other_button = Button(self, text="Restaurantes", command=self.restaurantes)
        self.other_button.place( x=10, y = 50)
        self.other_button.config(width=10, height=10)

        self.other_button = Button(self, text="Itens", command=self.itens)
        self.other_button.pack(side="left")
        self.other_button.place( x=110, y = 50)
        self.other_button.config(width=10, height=10)

        self.other_button = Button(self, text="Ementas", command=self.ementas)
        self.other_button.pack(side="left")
        self.other_button.place( x=210, y = 50)
        self.other_button.config(width=10, height=10)

        self.close_button = Button(self, text="Sair", command=self.endApp)
        self.close_button.pack(side="left")

        self.close_button.place( x=210, y = 280)
        self.close_button.config(width=10, height=5)

    def endApp(self):
        os._exit(1)

    def restaurantes(self):
        self._second_window = Rt.restaurante()
        self.destroy()

    def itens(self):
        self._third_window = It.item()
        self.destroy()

    def ementas(self):
       self._fourth_window = Et.ementa()
       self.destroy()

 

def mainInterface(root):
    my_gui = ecran_entrada(root)
    


if __name__ == '__main__':
    window = ecran_entrada()
    window.mainloop()
