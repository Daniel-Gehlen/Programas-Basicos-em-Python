# O seaborn é uma biblioteca de visualização baseada no matplotlib, que oferece uma interface
# de alto nível para criar gráficos estatísticos atraentes. Vamos criar um exemplo usando 
# o seaborn para criar um gráfico de dispersão com uma linha de regressão:

import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
idade = [25, 30, 22, 35, 40, 28, 18, 50]
salario = [50000, 60000, 40000, 75000, 80000, 55000, 35000, 90000]

# Criando um gráfico de dispersão com uma linha de regressão
sns.set(style='whitegrid')
sns.regplot(x=idade, y=salario)
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Relação entre Idade e Salário')
plt.show()


# Neste exemplo, usamos a função regplot() do seaborn para criar um gráfico de dispersão
# com uma linha de regressão que mostra a relação entre idade e salário.

# Ambos os exemplos ilustram como as bibliotecas matplotlib e seaborn podem ser usadas
# para criar visualizações de dados de forma eficaz em Python. As saídas gráficas resultantes 
# desses exemplos ajudam a compreender os dados e as tendências de maneira mais visual 
# e informativa.