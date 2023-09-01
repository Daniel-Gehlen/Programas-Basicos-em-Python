# Aqui temos três classes: Vehicle, Car e Motorcycle. A classe Vehicle é a superclasse base, 
# enquanto Car e Motorcycle são subclasses que herdam de Vehicle.

# Vehicle possui métodos para iniciar e parar o motor.
# Car herda de Vehicle e adiciona métodos para abrir e fechar portas.
# Motorcycle também herda de Vehicle e possui um método específico para fazer uma "wheelie" 
# (manobra de moto).

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting.")

    def stop_engine(self):
        print(f"The {self.brand} {self.model}'s engine is stopping.")


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def open_doors(self):
        print(f"Opening the {self.num_doors} doors of the {self.brand} {self.model}.")

    def close_doors(self):
        print(f"Closing the {self.num_doors} doors of the {self.brand} {self.model}.")


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def wheelie(self):
        print(f"The {self.brand} {self.model} is performing a wheelie!")

#Aqui está como você pode usar essas classes:

my_car = Car("Toyota", "Camry", 4)
my_motorcycle = Motorcycle("Harley-Davidson", "Sportster")

my_car.start_engine()
my_car.open_doors()

my_motorcycle.start_engine()
my_motorcycle.wheelie()


