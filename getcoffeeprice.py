from tkinter import *

g = Tk()
g.title('Gui')
g.geometry('800x400')

br=Button(g,text='Pare',bg='red',fg='white').pack()
by=Button(g,text='Atenção',bg='yellow',fg='green').pack()
bg=Button(g,text='Siga',bg='green',fg='white').pack()
bg.place(x=200,y=200)
g.mailoop()

