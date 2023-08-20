import sqlite3

conn = sqlite3.connect(áulaDB.db)

#CRUD-CREATE
cursor = conn.cursor()
cursor.execute(´´´)
INSERT  INTO fornecedor (nome_fornecedor, cnpj, cidade, estado, cep, data_cadastro)
VALUES ('Empresa A', '11.111.111/1111-1', 'São Paulo', 'SP', '11111-111', '2020-01-01')
''')
conn.commit()

#READ
cursor.execute('SELECT * FROM fornecedor')
resultado = cursor.fetchall()
for linha in resultado:
print(linha)

#UPDATE
cursor.execute('UPDATE fornecedor SET cidade = 'Campinas' WHERE id_fornecedor = 5')
conn.commit()

#DELETE
cursor.execute('DELETE FROM fornecedor WHERE id_fornecedor = 2')
conn.commit

