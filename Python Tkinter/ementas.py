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

        self.geometry("800x400+30+30")

        #Ligação
        #conn = psycopg2.connect(host="localhost",database="Restaurante", user="R&R_admin", password="estgv16790")
        #self.cur = conn.cursor()

        self.other_button = Button(self, text="Criar ementa", command=self.criarementa, width=15, height = 3)
        self.other_button.grid(row = 1, column = 1) 
        self.close_button = Button(self, text="Voltar atrás", command=self.goback, width=15, height = 1)
        self.close_button.grid(row = 2, column = 1)
        self.close_button = Button(self, text="Sair", command=self.endApp, width=15, height = 1)  
        self.close_button.grid(row = 3, column = 1)

        coluna1 = Label(self, text="Tipo de ementa", width=20)
        coluna1.grid(row = 1, column = 3)
        coluna2 = Label(self, text="Tipo de refeição", width=20)
        coluna2.grid(row = 1, column = 4)
        coluna3 = Label(self, text="Designação", width=20)
        coluna3.grid(row = 1, column = 5)

        self.mostrar_ementas()

        self.grid_rowconfigure(1, minsize=25) 
        self.grid_columnconfigure(2, minsize=20)

        #conn.close()

    def endApp(self):
        os._exit(1)

    def goback(self):
        self._second_window = Menu.ecran_entrada()
        self.destroy()

    def mostrar_ementas(self):
        #data = self.ler_ementas()
        data = "isto eum teste"
        for index, dat in enumerate(data):
            Label(self, text = "ola").grid(row = index + 2, column = 3)
            Label(self, text = "ola1").grid(row = index + 2, column = 4)
            Label(self, text = "ola2").grid(row = index + 2, column = 5)
            #Label(self, text = dat[0]).grid(row = index + 2, column = 3)
            #Label(self, text = dat[1]).grid(row = index + 2, column = 4)
            #Label(self, text = dat[2]).grid(row = index + 2, column = 5)

     
    #def ler_ementas(self):
        #self.cur.execute("select * from ementas limit 10")
        #return self.cur.fetchall()
        
    def criarementa(self):
        self._third_window = Ce.criarementa()
        self.destroy()

if __name__ == '__main__':
    window = ementa()
    window.mainloop()

