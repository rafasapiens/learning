import sqlite3
import time
import datetime


connection=sqlite3.connect('Cadastro.db')
c=connection.cursor()

#SQL

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS dados(Empresa text, CNPJ real, Razão_Social text, datestamp text, value real)')

create_table()


data_Empresa= 'EcoBusiness Consultoria'
CNPJ='11.134.214/0001-99'
Razão_Social='EcoBusiness Consultoria Ltda'
value=4




def dataentry():

#inserção de dados manual
    ''' c.execute("INSERT INTO dados VALUES(1, 1365952181.288, 'Python Sentiment', '2018-10-18 21:05:35', 5)")

    c.execute("INSERT INTO dados VALUES(2, 1365952257.905, 'Python Sentiment', '2018-10-18 21:10:35', 6)")

    c.execute("INSERT INTO dados VALUES(3, 1365952264.123, 'Python Sentiment', '2018-10-18 21:11:35', 4)")

    connection.commit()
    '''
#inserção de dados dinamicamente
    date= str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%d-%m-%Y %H:%M:%S'))

    c.execute('INSERT INTO dados (Empresa, CNPJ, Razão_Social, datestamp, value) VALUES (?,?,?,?,?)',(data_Empresa, CNPJ, Razão_Social, date, value))

    connection.commit()


    

dataentry()
