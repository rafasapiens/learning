print("-----------------------------------------------------")
print("---------Sistema para cadastro de pessoas -----------")
print("-----------------------------------------------------")

from tkinter import *
formPessoa = Tk()
formPessoa.title("Cadastro de Pessoas")
formPessoa.geometry("400x250+300+200") #coluna+linha

#titulo
titulo = Label(formPessoa,text="Cadastro de Pessoas:")
titulo.grid(row=0,stick=W+E+N+S,pady=10,padx=10)
separa = Frame(height=2, bd=1, relief=SUNKEN)
separa.grid(row=1,stick=W+E+N+S,columnspan=4)

#pesquisa
labelpesquisa = Label(formPessoa,text="Pesquisar:")
labelpesquisa.grid(row=2,column=0,pady=15)
#campo de pesquisa
editpesquisa = Entry()
editpesquisa.grid(row=2,column=1,pady=15)
#botão de pesquisa
botaopesquisa = Button(formPessoa,text="Pesquisar")
botaopesquisa.grid(row=2,column=3,padx=10,pady=15)

#labels pessoa
labelnome = Label(formPessoa,text="Nome..: ")
labelfone = Label(formPessoa,text="Fone..: ")
labelemail = Label(formPessoa,text="Email..: ")

#entradas (Entry)
editnome = Entry()
editfone = Entry()
editemail = Entry()

#posicionamento no formulário dos label e entradas de pessoa
labelnome.grid(row=4,stick=W,padx=10)
editnome.grid(row=4,column=1,pady=5)
labelfone.grid(row=5,stick=W,padx=10)
editfone.grid(row=5,column=1,pady=5)
labelemail.grid(row=6,stick=W,padx=10)
editemail.grid(row=6,column=1,pady=5)

#botoes para manutencao de pessoas
botoes = Frame()
botaoNovo = Button(botoes,text="Novo")
botaoGravar = Button(botoes,text="Gravar")
botaoAlterar = Button(botoes,text="Alterar")
botaoExcluir = Button(botoes,text="Excluir")

#posicionamento dos botoes
botaoNovo.grid(row=1,column=0,pady=10)
botaoGravar.grid(row=1,column=1,pady=10,padx=2)
botaoAlterar.grid(row=1,column=2,pady=10,padx=2)
botaoExcluir.grid(row=1,column=3,pady=10,padx=2)

separa1 = Frame(height=2, bd=1, relief=SUNKEN)
separa1.grid(row=8,stick=W+E+N+S,columnspan=4,pady=5)

botoes.grid(row=9,column=1)

mainloop()
