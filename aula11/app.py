from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'chave_flask_super_secreta'  # Necessário para usar session

db_config = {
    'user': 'python',
    'password': 'aula@123',
    'host': 'exemploaulacaio.mysql.database.azure.com',
    'port': 3306,
    'database': 'escolasenac'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')

        # Inserir no banco
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s)"
        cursor.execute(query, (usuario, senha))
        cnx.commit()
        cursor.close()
        cnx.close()

        # Após cadastrar, redireciona para página inicial ou outra
        return redirect(url_for('index'))
    else:
        return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
                        # verifica credencias no banco de dados
        cnx = mysql.connector.connect(**db_config)
        cursor = cnx.cursor()
        query = "SELECT COUNT(*) FROM usuario_secretaria WHERE usuario = %s AND senha = %s "
        cursor.execute(query, (usuario, senha))
        result = cursor.fetchone()
        cursor.close()
        cnx.close()

        if result and result[0] == 1:
            # login OK -->> guarda na sessão
            session['usuario_logado'] = usuario
            return redirect(url_for('home'))
        else:
            return render_template('login.html', erro="usuario ou senha incorretos. ")
        
    else:
        return render_template('login.html')
    
if __name__ == '__main__' :
    app.run(debug=True)