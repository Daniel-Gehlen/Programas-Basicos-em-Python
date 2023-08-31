# Tanto o método apply() quanto o método map() são usados para aplicar uma função a elementos 
# de uma série ou coluna em um DataFrame do pandas. No entanto, eles têm algumas diferenças
# na forma como são aplicados e nos tipos de objetos aos quais podem ser aplicados.

# O método map() é usado principalmente para substituir valores em uma série ou coluna usando 
#um dicionário ou uma função. Ele pode ser aplicado apenas a objetos do tipo série.

# Vamos dar uma olhada em um exemplo que usa o método map() para substituir nomes de países por 
#seus códigos de país:


import pandas as pd

data = {'País': ['Brasil', 'Estados Unidos', 'Canadá', 'México']}
df = pd.DataFrame(data)

codigo_paises = {'Brasil': 'BR', 'Estados Unidos': 'US', 'Canadá': 'CA', 'México': 'MX'}

# Usando o método map() para substituir nomes de países por códigos
df['Código'] = df['País'].map(codigo_paises)

print(df)

# Neste exemplo, o método map() é usado para criar uma nova coluna "Código" no DataFrame,
# onde os nomes dos países são mapeados para seus códigos correspondentes.


# O método apply() é mais flexível e pode ser aplicado tanto a objetos do tipo série quanto 
# a colunas inteiras do DataFrame. Ele permite que você aplique uma função personalizada 
# a cada elemento da série ou coluna.

# Vamos dar uma olhada em um exemplo que usa o método apply() para calcular o comprimento 
# de cada nome de país:

import pandas as pd

data = {'País': ['Brasil', 'Estados Unidos', 'Canadá', 'México']}
df = pd.DataFrame(data)

# Usando o método apply() para calcular o comprimento de cada nome de país
df['Comprimento'] = df['País'].apply(len)

print(df)

# Neste exemplo, o método apply() é usado para aplicar a função len() a cada elemento da coluna 
# "País", resultando em uma nova coluna "Comprimento" que contém o comprimento de cada nome de 
# país.

# Em resumo:

# O map() é geralmente usado para substituir valores usando dicionários ou funções de mapeamento
# simples.

# O apply() é mais versátil e permite aplicar funções personalizadas a elementos individuais ou
# colunas inteiras do DataFrame.