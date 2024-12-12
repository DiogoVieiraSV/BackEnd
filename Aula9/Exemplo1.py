import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

idade_aluno = input("Digite a idade de deseja pesquisar: ")


#consulta parametrizada
query = f"SELECT  idade, endereço From Aluno WHERE idade = {idade_aluno} "
cursor.execute(query, (idade_aluno,))

resultados = cursor.fetchall()
if resultados:
    for cpf, endereco in resultados:
        print(f" cpf:  {cpf}, Endereço:  {endereco}")
else:
    print("não encontramos ninguem com essa idade")

cursor.close()
cnx.close()