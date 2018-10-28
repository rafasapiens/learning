from tkinter import *
class Sistema:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()
        self.menu = Menu(master)

        self.menuCadastro = Menu(self.menu)
        self.menuCadastro.add_command(label="Cadastro empresa (Check-list)")
        self.menuCadastro.add_command(label="Imprime Check-list")
        self.menuCadastro.add_command(label="Importar dados Check-list")
        self.menuCadastro.add_command(label="Gerar arquivo Check-list")
        self.menu.add_cascade(label="Cadastro",menu=self.menuCadastro)

        self.menuCadastroPPRA = Menu(self.menu)
        self.menuCadastroPPRA.add_command(label="Cadastro PPRA")
        self.menuCadastroPPRA.add_command(label="Imprime PPRA")
        self.menuCadastroPPRA.add_command(label="Importar dados PPRA")        
        self.menuCadastroPPRA.add_command(label="Gerar arquivo PPRA")
        self.menu.add_cascade(label="PPRA",menu=self.menuCadastroPPRA)

        self.menuAjuda = Menu(self.menu)
        self.menuAjuda.add_command(label="Ajuda")
        self.menu.add_cascade(label="Ajuda",menu=self.menuAjuda)



        master.config(menu=self.menu)







root = Tk()
root.geometry('600x400')
root.title('Sistema PPRA 1.0')
Sistema(root)
root.mainloop()
