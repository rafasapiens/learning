# !/usr/bin/python3
from tkinter import *

from tkinter import messagebox

top = Tk()
top.geometry("200x200")
def hello():
   messagebox.showinfo("Caixa de Mensagem", "Esta é uma caixa de mensagem de contaminação por virus. Pressione Ok para sair.")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 35,y = 50)

top.mainloop()

'''
from tkinter import *
import tkMessageBox
import sqlite3
import os
def dic_bd(bd, tabela):
   """
    Função que recebe o banco de dados como string (bd) e
    o nome da tabela como string (tabela) e
    retorna um dicionario com todos os itens da tabela consultada.
   """
   conect=sqlite3.connect(bd)
   c = conect.cursor()
   a={}
   for i in c.execute("SELECT * FROM %s" %tabela):
    a[i[0]]=[i[1],i[2]]
   conect.close()
   return a	   
#Criando banco de dados
#====================================================================#
conectar = sqlite3.connect("banco_dados.db")
c = conectar.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS produtos(id_produto INTEGER PRIMARY KEY AUTOINCREMENT, produto TEXT,ean REAL,ncm REAL)""")
c.execute("""CREATE TABLE IF NOT EXISTS usuarios(id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,nome TEXT,senha TEXT)""")
a=dic_bd("banco_dados.db", "usuarios")
if a == {}:
   c.execute("INSERT INTO usuarios VALUES (NULL,?,?)",("admin","admin"))
conectar.commit()
conectar.close ()
#====================================================================#
def center(win):
   #funçao para centralizar
   win.update_idletasks()
   width = win.winfo_width()
   frm_width = win.winfo_rootx() - win.winfo_x()
   win_width = width + 2 * frm_width
   height = win.winfo_height()
   titlebar_height = win.winfo_rooty() - win.winfo_y()
   win_height = height + titlebar_height + frm_width
   x = win.winfo_screenwidth() // 2 - win_width // 2
   y = win.winfo_screenheight() // 2 - win_height // 2
   win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

class login:
   acesso=0
   def __init__(self, janela):
    #==========================Configurações=============================#
    self.tentativas=3
    fonte = ('Arial','14')
    fontb = ('Arial','12')
    self.janela = janela
    self.janela.resizable(width=False, height=False)
    self.janela.title('Login')
    #==============================Frames================================#
    frame=Frame(self.janela,borderwidth=3, relief=RAISED)
    frame.pack(pady = 2, padx=2)
    titulo=Frame(frame)
    titulo.pack(pady = 1, padx=1)
    caixa=Frame(frame)
    caixa.pack(pady = 1, padx=1)
    #=============================Widgets================================#
    titulosis=Label(titulo, text='TESTE', font=fonte, fg="darkblue", width=13).grid(row=1, column=1, sticky=W, pady=3)
    name=Label(caixa, text='Nome').grid(row=1, column=1, sticky=W, pady=3)
    senha=Label(caixa, text='Senha').grid(row=2, column=1, sticky=W, pady=3)
    self.entry_name=Entry(caixa, width=10)
    self.entry_name.grid(row=1, column=2, sticky=W, pady=3)
    self.entry_name.focus_force()
    self.entry_senha = Entry(caixa, width=10, show='*')
    self.entry_senha.grid(row=2, column=2, sticky=W, pady=3)
    entrar=Button(caixa, width=8, command=self.Entrar, text="Entrar")
    entrar.grid(row=3, column=1, sticky=W, pady=3)
    sair=Button(caixa, width=8, command=self.Sair, text="Sair")
    sair.grid(row=3, column=2, sticky=W, pady=3)
   def Entrar(self):
    loguin = self.entry_name.get()
    senha = self.entry_senha.get()
    a=dic_bd("banco_dados.db", "usuarios")
    con=0
    for i in a:
	    if a[i][0] == loguin:
		    if a[i][1] == senha:
			    con=1				   
    if con==1:
	    self.janela.destroy()
	    Programa()		   
    else:
	    self.tentativas=self.tentativas-1
	    tkMessageBox.showerror('Senha  ou usuario invalido', 'Este usuario ou esta senha é invalida.\nVocê só pode tentar mais %i vezes' %self.tentativas)
	    if self.tentativas <=0:
		    self.janela.destroy()

   def Sair(self):
    self.janela.destroy()

class teste:
   def __init__(self, janela):


    #==========================Configurações=============================#
    self.abas = Notebook(janela)
    janela.resizable(width=False, height=False)
    janela.title('teste')
    font = ('Arial','14')
    fontb = ('Arial','12')
    #==============================Frames================================#
    caixa=LabelFrame(self.abas)
    caixa.grid(pady=5)
    caixa2=LabelFrame(self.abas)
    caixa2.grid()

    #=============================Widgets================================#
    self.abas.add(caixa,text='Pessoal')
    self.abas.add(caixa2,text='Cadastros')
    #abas.add(self.frame_aba3,text='Util')
    self.abas.grid()
def Login():	
   raiz=Tk()
   acesso=login(raiz)
   center(raiz)
   raiz.mainloop()
   return acesso.acesso
def Programa():	
   raiz=Tk()
   raiz.geometry('500x400')
   acesso=teste(raiz)
   center(raiz)
   raiz.mainloop()
Login()
'''
