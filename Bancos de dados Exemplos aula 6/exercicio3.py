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
query1 = "SELECT nome, naturalidade FROM aluno WHERE naturalidade LiKE 'rio de janeiro' AND sexo LIKE 'M';"

cursor.execute(query1)

# Processar os resultados
resultados1 = cursor.fetchall()

query2 = "SELECT nome, naturalidade FROM aluno WHERE naturalidade LiKE 'são paulo' AND sexo LIKE 'F';"

cursor.execute(query2)

# Processar os resultados
resultados2 = cursor.fetchall()



# Classificação dos alunos
for nome, naturalidade in resultados1:
   print(nome, naturalidade)

for nome, naturalidade in resultados2:
   print(nome, naturalidade)
       
    

# Fechando o cursor e a conexão
cursor.close()
cnx.close()