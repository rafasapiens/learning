import sqlite3

connection=sqlite3.connect('tutorial.db')
c=connection.cursor()

#SQL consulta do banco de dados
sql = 'SELECT * FROM dados WHERE keyword = ?'

sql2='SELECT * FROM dados WHERE keyword = ? and value=? and id=?'

def read_data(wordUsed):
    for row in c.execute(sql, (wordUsed,)):
        print (row)


    print ('===============########=================')
    for row in c.execute(sql2, ('Python Sentiment', 4, 3)):
        print(row)

read_data('Python is awesome!')
        
