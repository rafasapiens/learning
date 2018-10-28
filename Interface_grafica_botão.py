from tkinter import *

g = Tk()
g.title('Semáforo')
g.geometry('200x100')

br=Button(g,text='Pare',bg='red',fg='white').pack()
by=Button(g,text='Atenção',bg='yellow',fg='green').pack()
bs=Button(g,text='Siga',bg='green',fg='white').pack()
bs.place(x=50,y=100)
g.mailoop()

