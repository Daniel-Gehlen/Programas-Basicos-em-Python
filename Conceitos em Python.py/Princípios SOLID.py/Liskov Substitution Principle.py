class Bird:
    def fly(self):
        return "Voando"

class Sparrow(Bird):
    def fly(self):
        return "Pardal voando"

class Ostrich(Bird):
    def fly(self):
        return "Avestruz não pode voar"

def bird_in_action(bird):
    return bird.fly()

sparrow = Sparrow()
ostrich = Ostrich()

print("Ação do pardal:", bird_in_action(sparrow))
print("Ação do avestruz:", bird_in_action(ostrich))

# Um exemplo que demonstra o Princípio da Substituição de Liskov:

# Neste exemplo, as classes Sparrow e Ostrich herdam da classe base Bird. No entanto, o avestruz
# não pode voar, o que é representado pela implementação da função fly() na classe Ostrich.

# O princípio é atendido porque podemos substituir um objeto Sparrow ou Ostrich por 
# um objeto Bird na função bird_in_action() sem afetar a integridade do programa. Isso ocorre
# porque o método fly() é implementado de maneira apropriada para cada tipo de ave, e o 
# comportamento esperado não é quebrado.

# O código exemplifica que as classes derivadas são substituíveis pelas classes base sem causar
# problemas, mantendo assim a coesão do programa.