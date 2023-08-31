import sqlite3

# Conectar ao banco de dados (será criado se não existir)
conn = sqlite3.connect('exemplo.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar uma tabela (caso ela ainda não exista)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
    )
''')

# Inserir alguns dados na tabela
cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', ('Alice', 25))
cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', ('Bob', 22))
cursor.execute('INSERT INTO alunos (nome, idade) VALUES (?, ?)', ('Carol', 28))

# Commit as alterações no banco de dados
conn.commit()

# Executar uma consulta para retornar todos os alunos
cursor.execute('SELECT * FROM alunos')
alunos = cursor.fetchall()

# Imprimir os dados retornados
for aluno in alunos:
    print(f'ID: {aluno[0]}, Nome: {aluno[1]}, Idade: {aluno[2]}')

# Fechar a conexão com o banco de dados
conn.close()


#Aqui está um exemplo de código em Python que utiliza o módulo sqlite3 para se conectar a um
# banco de dados SQLite, realizar consultas e retornar dados:

# Neste exemplo, estamos utilizando o SQLite como o DBMS. Primeiro, conectamos ao banco de dados
# (ou o criamos caso não exista) e criamos uma tabela chamada "alunos". Em seguida, inserimos 
# alguns registros nessa tabela. Depois, realizamos uma consulta para selecionar todos
# os registros da tabela "alunos" e utilizamos o método fetchall() para obter os dados 
# retornados pela consulta. Finalmente, imprimimos os dados na saída.

# Lembre-se de que esse é apenas um exemplo básico. Sistemas de gerenciamento de banco de dados
# mais complexos podem envolver esquemas mais elaborados, consultas mais avançadas e lidar com
# questões de segurança, escalabilidade e otimização.