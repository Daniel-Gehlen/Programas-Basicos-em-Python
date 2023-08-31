class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Atributo privado com dois underscores iniciais

    # Método público para obter a idade
    def get_age(self):
        return self.__age

    # Método público para definir a idade
    def set_age(self, new_age):
        if new_age > 0:
            self.__age = new_age
        else:
            print("Idade inválida!")

# Criando um objeto Person
person = Person("João", 25)

# Tentando acessar o atributo privado diretamente (isso causará um erro)
# print(person.__age)  # Isso resultará em um erro de atributo

# Usando o método público para obter a idade
print(f"{person.name} tem {person.get_age()} anos.")

# Usando o método público para definir uma nova idade
person.set_age(30)

# Usando o método público para obter a nova idade
print(f"{person.name} agora tem {person.get_age()} anos.")


# A classe chamada Person (Pessoa) que tem um atributo privado chamado __age (idade). 
# Vamos usar métodos públicos para definir e obter a idade, demonstrando assim 
# o conceito de encapsulamento.


# Neste exemplo, o atributo __age é definido como privado usando dois underscores iniciais (__). 
# Isso faz com que ele não seja acessível diretamente fora da classe. 
# Os métodos públicos get_age e set_age são usados para obter e definir a idade, respectivamente.
# Isso encapsula o acesso ao atributo __age e protege seu estado, permitindo que 
# as operações sejam realizadas de maneira controlada.

# Note que, em Python, os atributos privados ainda podem ser acessados de fora da classe 
# usando uma notação específica (_NomeDaClasse__atributo). No entanto, essa não é uma prática 
# recomendada e vai contra o princípio de encapsulamento.

# Lembrando que esse é um exemplo básico para ilustrar o conceito de encapsulamento. 
# Em cenários mais complexos, você pode usar propriedades, getters e setters para melhorar 
# a implementação do encapsulamento.