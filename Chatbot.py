#Chatbot  ==== minha tentativa de criar um chat interativo com um usuário#

print ("Opa vc está aí!")

nome=str(input('Olá amigo, qual seu nome? \n'))

print ("Prazer", nome,'!'"""\nEu sou o computador, \nmas pode me chamar de Amigão.
       \nAdoro quando me chamam assim! ;)\n""" )
idade = int(input('Qual sua idade? \n'))

print ('Muito jovem ainda! \nTemos muito o que viver juntos!')

from tkinter import *

janela=Tk()

janela.title("Meu novo amiguinho")

janela.geometry('500x500')

janela.mainloop()

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Olá Amiguinho\n(click aqui para iniciar)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("Ai, isso faz cosquinha!")

root = tk.Tk()
app = Application(master=root)
app.mainloop()

