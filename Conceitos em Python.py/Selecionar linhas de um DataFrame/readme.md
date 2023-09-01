# Selecionar linhas de um DataFrame com base em uma condição é uma operação comum ao trabalhar 
# com análise de dados usando o pandas.

# Suponha que temos um DataFrame que representa dados de alunos e queremos selecionar apenas
# os alunos com notas acima de 80:

import pandas as pd

data = {'Nome': ['Alice', 'Bob', 'Carol', 'David'],
        'Nota': [90, 75, 85, 60]}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print()

# Para selecionar linhas com base em uma condição, podemos usar a indexação booleana do pandas.
# Aqui está o código para isso:

# Selecionando linhas com notas acima de 80
notas_acima_de_80 = df[df['Nota'] > 80]

print("Alunos com notas acima de 80:")
print(notas_acima_de_80)

# Neste exemplo, a expressão df['Nota'] > 80 cria uma série booleana indicando quais linhas
# atendem à condição de ter notas acima de 80. Ao passar essa série como índice para o DataFrame
# df, obtemos apenas as linhas que satisfazem a condição.

# O DataFrame resultante contém apenas as linhas que atendem à condição de ter notas acima de 80.

# Essa técnica de indexação booleana é muito poderosa e flexível, pois você pode aplicar várias
# condições e combinações para selecionar linhas específicas do DataFrame com base nos critérios
# desejados.