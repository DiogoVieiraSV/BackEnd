import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

idade = input("Digite a idade dos alunos ")


#consulta parametrizada
query = "SELECT cpf, endereco From Aluno WHERE idade = %s;"
cursor.execute(query, (idade,))

resultados = cursor.fetchall()
if resultados:
    for cpf, endereco in resultados:
        print(f"endereco: {endereco}, cpf:  {cpf},")
else:
    print("Nenhum aluno encontrado com esse nome.")

cursor.close()
cnx.close()