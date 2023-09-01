# O matplotlib é uma biblioteca de visualização de dados amplamente usada que oferece uma ampla 
# variedade de gráficos e plotagens. Aqui está um exemplo simples usando o matplotlib para criar
# um gráfico de barras:

import matplotlib.pyplot as plt

# Dados de exemplo
cidades = ['Nova Iorque', 'Los Angeles', 'Chicago', 'Houston', 'Miami']
populacao = [8175133, 3792621, 2695598, 2099451, 1420491]

# Criando um gráfico de barras
plt.bar(cidades, populacao)
plt.xlabel('Cidades')
plt.ylabel('População')
plt.title('População de algumas cidades dos EUA')
plt.show()

# Neste exemplo, usamos a função bar() do matplotlib para criar um gráfico de barras mostrando 
# a população de algumas cidades dos EUA.