class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class EmailSender:
    def send_email(self, customer, message):
        # Lógica para enviar um email para o cliente
        print(f"Enviando e-mail para {customer.name} - Mensagem: {message}")

class CustomerService:
    def __init__(self):
        self.email_sender = EmailSender()

    def create_customer(self, name, email):
        customer = Customer(name, email)
        # Lógica para salvar o cliente em um banco de dados
        print(f"Cliente {customer.name} criado com sucesso!")
        self.email_sender.send_email(customer, "Bem-vindo ao nosso serviço!")

service = CustomerService()
service.create_customer("João", "joao@example.com")

# Single Responsibility Principle (Princípio da Responsabilidade Única):

# Este princípio prega que uma classe deve ter apenas uma razão para mudar, ou seja,
# deve ter uma única responsabilidade.

# Neste exemplo, aplicamos o Princípio da Responsabilidade Única. A classe Customer é responsável
# apenas por representar os dados do cliente. A classe EmailSender é responsável apenas por
# enviar emails. A classe CustomerService é responsável por criar clientes e usar 
# o EmailSender para enviar um email de boas-vindas. Cada classe tem uma única responsabilidade
# bem definida.

# Quando executamos o código, ele criará um cliente chamado "João" e enviará um email de
# boas-vindas para ele.

# A divisão das responsabilidades em classes separadas torna o código mais modular, 
# facilitando a manutenção e a extensibilidade. Se a lógica de envio de email precisar ser 
# alterada, isso não afetará o restante do código relacionado aos clientes.