vogais = ['a', 'e', 'i', 'o', 'u']

# Pode ser cirada depois
vogais = []
vogais.append('a')
vogais.append('e')
vogais.append('i')
vogais.append('0')
vogais.append('u')

#Para acessar um item da lista
vogais['3']
vogais['3':]

#Uma maneira elegante de criar lista é olist comprehenson
[item for item in lista]

[2*x for x in range(10)]

# Tuplas imutáveis colondo entre parênteses
vogais = ('a', 'e,', 'i', 'o', 'u')

#Objeto do tipo set habilita operações matemáticas de conjuntos, como união, interecção, diferença, etc
#Colocando os valores entre chaves
vogais = {'a', 'e,', 'i', 'o', 'u'}

#Com dict para fazer um mapeament entre chaves
cadastro = {'nome': 'João', 'idade':30, 'cidade': 'São Paulo'}

# para acessar um valor em um dicionário
nome_dicionario[chave] = novo_valor
