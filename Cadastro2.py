import sqlite3, time

conectar = sqlite3.connect('Cadastro2.db')
c = conectar.cursor()

def criar_db():
    c.execute('CREATE TABLE IF NOT EXISTS cadastro(nome text, telefone varchar, email text, data text)')
try:
    criar_db()
except:
    print('Erro ao criar banco de dados! :(')
else:
    print('Banco de dados iniciado com sucesso! :)')




def inserir (n,t,e):
    d = time.strftime('%d/%m/%Y %H:%M:%S')
    c.execute('INSERT INTO cadastro VALUES(?,?,?,?)',(n,t,e,d))
    conectar.commit()

fc =int(input('1 - Cadastrar\n2 - Pesquisar\nO que você deseja fazer?: '))

if fc == 1:
    try:
        print('Cadastro de Clientes')
        time.sleep(2)
        n = str(input('Insira Nome da Empresa: '))
        t = int(input('Insira Telefone: '))
        e = str(input('Insira o email: '))

        inserir (n,t,e)
    except:
        print('Erro ao cadastrar! :(')
    else:
        print('Cadastrado com Sucesso! ;)')
elif fc == 2:
    print('Aguarde!')
else:
    print('...')
  
