# !/usr/bin/python3
from tkinter import *
from tkinter import messagebox

top = Tk()
top.title('Caixa de mensagem')
top.geometry("300x100")


def hello():
    messagebox.showinfo("Caixa de Mensagem", "Se fudeu!\nEsta é uma caixa de mensagem de contaminação por virus. \nPressione Ok para finalizar a \nInstalação dos 8.574 viruses.")
    
B1 = Button(top, text = "Não Clique Aqui!", bg='red',fg='white', command = hello)
B1.place(x = 80,y = 50)


top.mainloop()

