from tkinter import *
import tkinter as tk
import os
import psycopg2
import menu as Menu

class restaurante(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Restaurantes")

        self.geometry("800x400+30+30")

        self.close_button = Button(self, text="Voltar atrás", command=self.goback)
        self.close_button.place( x=100, y = 280)
        self.close_button.config(width=10, height=3)

        self.close_button = Button(self, text="Sair", command=self.endApp)
        self.close_button.place( x=200, y = 280)
        self.close_button.config(width=10, height=3)

        conn = psycopg2.connect(host="basededados",database="Restaurante", user="R&R_admin", password="estgv16790")
        cur = conn.cursor()
        cur.execute("select * from restaurantes limit 10")
        cur.fetchall()
        conn.close()

    def endApp(self):
        os._exit(1)

    def goback(self):
        self._second_window = Menu.ecran_entrada()
        self.destroy()

if __name__ == '__main__':
    window = restaurante()
    window.mainloop()

