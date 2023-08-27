import sqlite3

conn = sqlite3.connect('aulaDB.db')

# Criando a tabela "fornecedor" se ela não existir
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS fornecedor (
        id_fornecedor INTEGER PRIMARY KEY,
        nome_fornecedor TEXT,
        cnpj TEXT,
        cidade TEXT,
        estado TEXT,
        cep TEXT,
        data_cadastro DATE
    )
''')
conn.commit()

# CRUD - CREATE
cursor.execute('''
    INSERT INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
    VALUES (?, ?, ?, ?, ?, ?)
''', ('Empresa A', '11.111.111/1111-1', 'São Paulo', 'SP', '11111-111', '2020-01-01'))
conn.commit()

# READ
cursor.execute('SELECT * FROM fornecedor')
resultado = cursor.fetchall()
print("Registros após inserção:")
for linha in resultado:
    print(linha)

# UPDATE
cursor.execute("UPDATE fornecedor SET cidade = ? WHERE id_fornecedor = ?", ('Campinas', 1))
conn.commit()

# DELETE
cursor.execute('DELETE FROM fornecedor WHERE id_fornecedor = ?', (1,))
conn.commit()

# READ novamente após atualização e exclusão
cursor.execute('SELECT * FROM fornecedor')
resultado = cursor.fetchall()
print("\nRegistros após atualização e exclusão:")
for linha in resultado:
    print(linha)

conn.close()