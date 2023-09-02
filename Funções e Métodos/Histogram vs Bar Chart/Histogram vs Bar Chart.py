import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados numéricos
data = np.random.normal(0, 1, 1000)  # Dados aleatórios com distribuição normal

# Criando um histograma
plt.hist(data, bins=20, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.show()

# Exemplo de dados categóricos
categories = ['A', 'B', 'C', 'D', 'E']
counts = [25, 40, 15, 30, 10]

# Criando um gráfico de barras
plt.bar(categories, counts, color='blue')
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Contagem')
plt.show()


# Tanto o histograma quanto o gráfico de barras são ferramentas de visualização de dados que exibem a distribuição de frequência de diferentes valores ou categorias. No entanto, eles são usados em contextos ligeiramente diferentes e têm características distintas.

# Histograma:

# Um histograma é usado principalmente para representar a distribuição de dados numéricos 
# contínuos ou discretos em intervalos (bins). Ele agrupa os dados em intervalos e mostra 
# a frequência ou contagem de ocorrências em cada intervalo. É especialmente útil para entender 
# a forma da distribuição dos dados e identificar tendências, padrões e outliers.

# Gráfico de Barras:

# Um gráfico de barras é usado para representar dados categóricos ou discretos. Cada categoria é
# representada por uma barra separada, e a altura da barra é proporcional à frequência 
# ou contagem da categoria correspondente. Gráficos de barras são frequentemente usados 
# para comparar diferentes categorias entre si.

# O que os dados retornam:

# No histograma, os dados retornam informações sobre a distribuição dos valores numéricos. 
# Você pode observar a concentração de valores em diferentes intervalos (bins) e avaliar 
# se a distribuição é simétrica, assimétrica, bimodal etc.

# No gráfico de barras, os dados retornam uma comparação visual das frequências ou contagens 
# das categorias. Isso permite identificar quais categorias são mais ou menos frequentes 
# e facilita a compreensão de relações entre diferentes categorias.

# A escolha entre um histograma e um gráfico de barras depende do tipo de dados que você está 
# lidando e dos insights que deseja obter da visualização.