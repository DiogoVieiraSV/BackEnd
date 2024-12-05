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
query = "SELECT nome, idade, tipo_sanguineo FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()


# Classificação dos alunos
for nome, idade, tipo_sanguineo in resultados:
    if (tipo_sanguineo in ["B+", "B-", "O-","O+"]):
        print("Doadores:", nome, idade, tipo_sanguineo)
       
    

# Fechando o cursor e a conexão
cursor.close()
cnx.close()