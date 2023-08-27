name = 'Guido'

for c in name:
    print(c)

name = 'Guido'
for i, c in enumerate(name):
    print(f'Posição = {i}, valor = {c}')

name = 'Guido'
for x in range(5):
    print(x)

# Exemplo de uso do break
disciplina = 'Linguagem de Programação'

for c in disciplina:
    if c == 'a':
        break
    else:
        print(c)

# Exemplo de uso do continue
disciplina = 'Linguagem de Programação'
for c in disciplina:
    if c == 'a':
        continue
    else:
        print(c)
