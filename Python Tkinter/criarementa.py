from tkinter import *
import tkinter as tk
import os
import psycopg2
import ementas as Et

class criarementa(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Criar Ementa")

        self.geometry("600x400+30+30")
        
        tipo_ref = StringVar(self)
        escolhas_refeicao = { 'Pequeno-almoço','Almoço','Jantar'}
        tipo_ref.set('Almoço') # Opção default

        popupMenu1 = OptionMenu(self, tipo_ref, *escolhas_refeicao, command = self.func)
        tiporefeicao = Label(self, text="Escolha o tipo de refeição")
        tiporefeicao.place(x = 15, y = 15)
        popupMenu1.place(x = 15, y = 45)

        tipo_eme = StringVar(self)
        escolhas_ementa = { 'Bebidas','Entradas','Pratos de Carne', 'Pratos de Peixe', 'Sobremesas'}
        tipo_eme.set('Bebidas') # Opção default

        popupMenu2 = OptionMenu(self, tipo_eme, *escolhas_ementa, command = self.func)
        tipoementa = Label(self, text="Escolha o tipo de ementa")
        tipoementa.place(x = 15, y = 90)
        popupMenu2.place(x = 15, y = 120)

        
        
        #Input nome ementa
        nomeementa_text = Label(text = "Nome da ementa * ",)
        nomeementa_text.place(x = 15, y = 160)
        nome_ementa = StringVar()
        nomeementa_entry = Entry(textvariable = nome_ementa, width = "30")
        nomeementa_entry.place(x = 15, y = 190)

        self.close_button = Button(self, text="Voltar atrás", command=self.goback)
        self.close_button.place( x=100, y = 280)
        self.close_button.config(width=10, height=3)

        self.close_button = Button(self, text="Sair", command=self.endApp)  
        self.close_button.place( x=200, y = 280)
        self.close_button.config(width=10, height=3)

    def endApp(self):
        os._exit(1)

    def goback(self):
        self._second_window = Et.ementa()
        self.destroy()

    def func(self,value):
        print (value)

    #def criarementa(self):
        #INSERT

def mainInterface(root):
    my_gui = ecran_entrada(root)
    


if __name__ == '__main__':
    window = criarementa()
    window.mainloop()

