vogais = ['a', 'e', 'i', 'o', 'u']

# Pode ser criada depois
vogais = []
vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('o')
vogais.append('u')

# Para acessar um item da lista
print(vogais[3])
print(vogais[3:])

# Uma maneira elegante de criar lista é com list comprehension
nova_lista = [item for item in vogais]
print(nova_lista)

nova_lista_multiplicada = [2*x for x in range(10)]
print(nova_lista_multiplicada)

# Tuplas imutáveis colocadas entre parênteses
vogais_tupla = ('a', 'e', 'i', 'o', 'u')

# Objeto do tipo set habilita operações matemáticas de conjuntos, como união, interseção, diferença, etc.
# Colocando os valores entre chaves
vogais_set = {'a', 'e', 'i', 'o', 'u'}

# Com dict, você pode fazer um mapeamento entre chaves
cadastro = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Para acessar um valor em um dicionário e atribuir um novo valor
cadastro['idade'] = 31

# Para imprimir algum resultado
print(cadastro)
