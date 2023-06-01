<h1 align="center"> Sistema básico de cadastro </h1>
<p align="center">
  
</p>
<p>Sistema feito em HTML, CSS e Python integrado ao banco de dados, para o estudo da linguagem e o desenvolvimento Web em Python utilizando o microframework Flask.</p>

<h1>Funcionalidades</h1>

- Cadastro de usuários: permite adicionar novos usuários ao banco de dados.
- Edição de usuários: possibilita editar informações de usuários existentes.
- Exclusão de usuários: permite remover usuários do banco de dados.
- Listagem de usuários: exibe todos os usuários cadastrados.

<h1>Tecnologias utilizadas</h1>

- HTML
- CSS
- Python
- Flask
- MySQL

<h1>Requisitos</h1>

<p>Certifique-se de ter as seguintes bibliotecas Python instaladas:</p>

- Flask
- Flask-WTF
- mysql-connector-python

<h1>Instalação</h1
  
1.Clone este repositório para o seu ambiente local
  
2.Navegue até o diretório clonado
  
3.Instale as dependências do Python: pip install -r requirements.txt
  
4.Configure as informações do banco de dados no arquivo app.py: 
  db_config = {
    'host': '127.0.0.1',
    'user': 'seu-usuario',
    'password': 'sua-senha',
    'database': 'nome-do-banco-de-dados'
}
 5.Crie a tabela no banco de dados: py app.py create_table 
  
 6.Inicie o servidor Flask: py app.py run
  
 7.Acesse o sistema no navegador: http://localhost:5000

  <h1>Contribuição</h1>
<p>Sinta-se à vontade para contribuir com melhorias, correções de bugs ou adição de novos recursos. Abra uma issue ou envie um pull request com as suas modificações.</p>


<h1>Observação</h1>
<p>Este é um projeto básico e não foi desenvolvido com foco em segurança ou performance. Utilize-o apenas para fins educacionais e de aprendizado.</p>
