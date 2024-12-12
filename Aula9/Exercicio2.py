import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()
print("Sistema de cadastro")
usuario = input("Nome de Usuario: ")
senha = input("senha:  ")
#consulta parametrizad
query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)" 

cursor.execute(query, (usuario,senha))
cnx.commit()

cursor.close()
cnx.close()