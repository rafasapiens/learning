from tkinter import *
class Login:
    def __init__(self, master):
        self.master = master
        self.master.title('Acesso ao sistema')

        Label(self.master,text='Usuário e Senha').grid(row=1, column=2, columnspan=1,pady=4)

        Label(self.master,text='Usuário:').grid(row=2,column=1,pady=4,padx=20)
        #não faça assim tudo junto pode da erro > self.usuario=Entry(self.master,width=10).grid(row=2,column=2)
        self.usuario=Entry(self.master,width=10)
        self.usuario.grid(row=2,column=2)
        self.usuario.focus_force()

        Label(self.master,text='Senha:').grid(row=3,column=1,pady=4)
        self.senha=Entry(self.master,width=10, show='*',fg='darkgrey',font=('Windings','10'))
        self.senha.grid(row=3,column=2)

        Label(self.master,text='Status...').grid(row=4,column=1,columnspan=2,pady=4)

        self.entrar=Button(self.master, width=7,text='OK')
        self.entrar.grid(row=5,column=2,pady=4,padx=3)
        self.sair=Button(self.master, width=7,text='Sair')
        self.sair.grid(row=5,column=3,pady=4,padx=3)


root=Tk()
Login(root)
root.geometry('300x170')
root.mainloop()
        
