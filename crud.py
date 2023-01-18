import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='bdcrud',
)

cursor = conexao.cursor()

#CRUD

#CREATE

nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")'
cursor.execute(comando)
conexao.commit() #Para editar o banco de dados

#READ

comando = f'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall() #Para ler o banco de dados
print(resultado)

#UPDATE

nome_produto = "banana"
valor = 6
comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

#DELETE
nome_produto = "nome_produto"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

cursor.close()
conexao.close()