from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

class Manager(ABC):
    @abstractmethod
    def manage(self):
        pass

class Employee(Worker):
    def work(self):
        return "Realizando tarefas como funcionário"

class Supervisor(Worker, Manager):
    def work(self):
        return "Supervisionando as operações"

    def manage(self):
        return "Gerenciando a equipe"

employee = Employee()
supervisor = Supervisor()

print("Funcionário:", employee.work())

# Como Supervisor é um tipo de Worker e Manager, ele pode realizar ambas as ações
print("Supervisor:", supervisor.work())
print("Supervisor (gerenciamento):", supervisor.manage())


# Neste exemplo, temos duas interfaces: Worker e Manager. A classe Employee implementa apenas 
# a interface Worker, já que um funcionário não precisa gerenciar. A classe Supervisor 
# implementa ambas as interfaces, Worker e Manager, pois realiza ambas as funções.

# O princípio é atendido porque a classe Employee não é forçada a implementar a função de 
# gerenciamento que não é relevante para ela. A segregação de interfaces permite que cada classe
# implemente apenas os métodos que são relevantes para sua funcionalidade, evitando a sobrecarga
# desnecessária de implementações.

# Portanto, o código exemplifica que as classes implementam apenas as interfaces relevantes para
# suas responsabilidades, seguindo o Princípio da Segregação de Interfaces.