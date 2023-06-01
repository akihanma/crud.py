from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import mysql.connector

app = Flask(__name__)
app.secret_key = 'senha'
app.template_folder = 'templates'

db_config = {
    'host': '*****',
    'user': '*****',
    'password': '*****',
    'database': '*****'
}

class EditForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    submit = SubmitField('Salvar')


def create_table():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                     (id INT AUTO_INCREMENT PRIMARY KEY,
                     nome VARCHAR(255) NOT NULL,
                     email VARCHAR(255) NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    email = request.form['email']
    
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome, email) VALUES (%s, %s)", (nome, email))
    conn.commit()
    conn.close()
    
    return redirect('/')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=%s", (id,))
    row = cursor.fetchone()
    conn.close()

    form = EditForm()

    if request.method == 'POST' and form.validate_on_submit():
        nome = form.nome.data
        email = form.email.data

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE usuarios SET nome=%s, email=%s WHERE id=%s", (nome, email, id))
        conn.commit()
        conn.close()

        return redirect('/')

    form.nome.data = row[1]
    form.email.data = row[2]

    return render_template('edit.html', form=form, row=row)


@app.route('/delete/<int:id>')
def delete(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
    conn.commit()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)