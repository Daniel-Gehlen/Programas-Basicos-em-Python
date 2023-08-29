# Suponha que temos um DataFrame que representa informações sobre alunos, onde alguns alunos 
# não têm uma nota atribuída:

import pandas as pd
import numpy as np

data = {'Nome': ['Alice', 'Bob', 'Carol', 'David'],
        'Idade': [25, np.nan, 22, 28],
        'Nota': [90, 75, np.nan, 60]}

df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print()

# O DataFrame tem uma coluna "Idade" e uma coluna "Nota", onde alguns valores estão ausentes 
# (representados por np.nan).

# Para lidar com os valores ausentes, podemos usar os seguintes métodos:

# 1 - isna() e notna(): Esses métodos retornam um DataFrame booleano, onde cada elemento indica 
# se é um valor ausente (True) ou não (False).

print("Verificando valores ausentes:")
print(df.isna())
print()

# 2 - dropna(): Este método permite remover linhas ou colunas com valores ausentes.

# Removendo linhas com pelo menos um valor ausente
df_sem_ausentes = df.dropna()

print("DataFrame após remover linhas com valores ausentes:")
print(df_sem_ausentes)
print()

# 3 - fillna(): Este método permite preencher os valores ausentes com algum valor específico.

# Preenchendo os valores ausentes na coluna "Nota" com a média das notas
media_notas = df['Nota'].mean()
df_preenchido = df.fillna({'Nota': media_notas})

print("DataFrame após preencher valores ausentes nas notas:")
print(df_preenchido)

# Lembrando que esses métodos retornam novos DataFrames ou realizam modificações no 
# DataFrame original, dependendo do caso.