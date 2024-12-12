import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="Python",
    password="aluno@123",
    host="exemploauladiogo.mysql.database.azure.com",
    port= 3306,
    database="escola",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, endereco FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, endereco in resultados:
    print(f"Nome do aluno: {nome}")
    print(f"Endereço: {endereco}")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()