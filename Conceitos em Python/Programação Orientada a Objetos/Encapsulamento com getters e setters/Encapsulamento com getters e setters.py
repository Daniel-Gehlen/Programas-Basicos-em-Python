class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    # Getter para a propriedade account_number
    @property
    def account_number(self):
        return self.__account_number

    # Getter para a propriedade balance
    @property
    def balance(self):
        return self.__balance

    # Setter para a propriedade balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Saldo inválido!")

    # Método para fazer um saque
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Saque de {amount} realizado com sucesso.")
        else:
            print("Saque inválido.")

    # Método para fazer um depósito
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Depósito de {amount} realizado com sucesso.")
        else:
            print("Depósito inválido.")

# Criando uma conta bancária
account = BankAccount("123456789", 1000.0)

# Usando a propriedade account_number (getter)
print("Número da conta:", account.account_number)

# Usando a propriedade balance (getter)
print("Saldo atual:", account.balance)

# Tentando definir um novo saldo inválido (isso vai disparar o setter)
account.balance = -500.0

# Fazendo um saque
account.withdraw(200)

# Fazendo um depósito
account.deposit(500)

# Verificando o saldo novamente
print("Saldo atual:", account.balance)

# Neste exemplo, a classe BankAccount representa uma conta bancária com um número de conta 
# e um saldo. Usamos propriedades para encapsular o acesso aos atributos privados
# __account_number e __balance. Isso melhora a legibilidade do código e mantém a interface 
# de acesso mais clara.

# O método @property é um decorador que transforma o método em uma propriedade somente leitura.
# No caso, os métodos account_number e balance são transformados em propriedades que permitem
# a leitura dos valores privados correspondentes.

# O decorador @balance.setter é usado para criar um método setter para a propriedade balance. 
# Isso nos permite controlar a validade dos valores ao definir o saldo.

# Usar propriedades, getters e setters ajuda a manter um controle rigoroso sobre o acesso 
# aos atributos de uma classe, melhorando a encapsulação e garantindo que as operações ocorram 
# de acordo com as regras definidas.