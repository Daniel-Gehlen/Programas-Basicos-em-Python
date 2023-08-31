class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

class Cow(Animal):
    def make_sound(self):
        return "Moo!"

# Função que recebe um animal e faz o animal fazer um som
def animal_sound(animal):
    return animal.make_sound()

# Criando instâncias das classes
dog = Dog()
cat = Cat()
cow = Cow()

# Chamando a função de fazer som para diferentes animais
print(animal_sound(dog))  # Saída: Woof!
print(animal_sound(cat))  # Saída: Meow!
print(animal_sound(cow))  # Saída: Moo!

# Neste exemplo, temos uma classe base Animal que define um método make_sound(). Em seguida,
# temos três subclasses Dog, Cat e Cow, cada uma delas sobrescreve o método make_sound()
# para retornar o som característico do respectivo animal.

# A função animal_sound() recebe um objeto do tipo Animal (ou qualquer uma de suas subclasses) 
# e chama o método make_sound(). O interessante aqui é que, embora a função animal_sound() 
# espere um objeto do tipo Animal, ela pode receber instâncias de suas subclasses 
# e chamar seus métodos específicos. Isso é possível devido ao polimorfismo, 
# onde objetos de diferentes classes podem ser tratados de maneira uniforme através de 
# uma interface comum.

# Assim, o polimorfismo permite que você escreva código mais genérico, reutilizável e flexível, 
# já que você pode trabalhar com classes diferentes de forma coesa, desde que elas compartilhem
# uma interface comum.