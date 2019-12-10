from tkinter import *
import tkinter as tk
import os
import psycopg2
import menu as Menu
import criarementa as Ce
import bd as BD

class ementa(tk.Tk):

    def __init__(self):
        super().__init__()
        
        self.title("Ementas")

        self.geometry("600x400+30+30")

        self.other_button = Button(self, text="Criar ementa", command=self.criarementa, width=15, height = 2)
        self.other_button.grid(row = 1, column = 1)

        self.grid_columnconfigure(2, minsize=80) 

        coluna1 = Label(self, text="Tipo de ementa")
        coluna1.grid(row = 1, column = 3)
        coluna2 = Label(self, text="Tipo de refeição")
        coluna2.grid(row = 1, column = 4)
        coluna3 = Label(self, text="Designação")
        coluna3.grid(row = 1, column = 5)

        self.grid_rowconfigure(2, minsize=250) 

        self.close_button = Button(self, text="Voltar atrás", command=self.goback, width=10, height = 2)
        self.close_button.grid(row = 3, column = 1)

        self.close_button = Button(self, text="Sair", command=self.endApp, width=10, height = 2)  
        self.close_button.grid(row = 3, column = 2)

    def endApp(self):
        os._exit(1)

    def goback(self):
        self._second_window = Menu.ecran_entrada()
        self.destroy()

    def criarementa(self):
        self._third_window = Ce.criarementa()
        self.destroy()

if __name__ == '__main__':
    window = ementa()
    window.mainloop()

