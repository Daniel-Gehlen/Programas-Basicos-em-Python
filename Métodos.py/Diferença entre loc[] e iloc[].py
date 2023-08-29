#loc[] e iloc[] são duas funções importantes do pandas, uma biblioteca em Python usada para 
#análise e manipulação de dados. Elas são utilizadas para acessar linhas e colunas de um 
#DataFrame, que é uma estrutura de dados tabular bidimensional.


import pandas as pd

# Criando um DataFrame de exemplo
data = {'Nome': ['Alice', 'Bob', 'Carol', 'David'],
        'Idade': [25, 30, 22, 28],
        'Cidade': ['São Paulo', 'Nova Iorque', 'Rio de Janeiro', 'Los Angeles']}

df = pd.DataFrame(data)

# Definindo o índice personalizado
df.set_index('Nome', inplace=True)

# Exibindo o DataFrame
print("DataFrame original:")
print(df)
print()

# Usando loc[] para acessar dados pelo rótulo do índice
print("Acessando dados com loc[]:")
print(df.loc['Bob'])
print()

# Usando iloc[] para acessar dados pelo índice inteiro
print("Acessando dados com iloc[]:")
print(df.iloc[2])

# Neste exemplo, criamos um DataFrame com informações fictícias sobre pessoas. Usamos o método 
# set_index() para definir a coluna "Nome" como o índice do DataFrame.

# Com loc[]: Podemos acessar linhas usando rótulos do índice. No exemplo, df.loc['Bob'] retorna 
# a linha correspondente aos dados de Bob.

# Com iloc[]: Podemos acessar linhas usando índices inteiros (posições). No exemplo, df.iloc[2]
#  retorna a terceira linha do DataFrame (índice 2), que corresponde aos dados de Carol.