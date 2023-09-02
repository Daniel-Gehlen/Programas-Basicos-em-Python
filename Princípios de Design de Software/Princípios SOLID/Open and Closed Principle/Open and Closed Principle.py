from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()

rectangle = Rectangle(5, 3)
circle = Circle(4)

calculator = AreaCalculator()
print("Área do retângulo:", calculator.calculate_area(rectangle))
print("Área do círculo:", calculator.calculate_area(circle))

# Neste exemplo, a classe Shape é aberta para extensão, pois novas formas geométricas 
# podem ser adicionadas (por exemplo, um triângulo) sem a necessidade de modificar o código 
# existente. Cada forma geométrica estende a classe abstrata Shape e implementa seu próprio 
# método area().

# O princípio é atendido porque, ao adicionar novas formas, não precisamos alterar o código 
# do AreaCalculator. Ele continua a funcionar com as novas formas adicionadas.

# O método calculate_area() no AreaCalculator utiliza polimorfismo para calcular a área
# de qualquer forma que implemente a interface Shape, sem a necessidade de modificar o código
# do calculador quando novas formas são introduzidas. Isso mantém o código aberto para 
# extensões, mas fechado para modificações diretas nos componentes existentes.