class ClassName:
    _Statement = None

class PrimeiraClasse:
    nome = None

    def imprimir_mensagem(self):
        print('Olá, seja bem-vindo!')

objeto1 = PrimeiraClasse()
objeto1.nome = 'Aluno 1'

print(objeto1.nome)
objeto1.imprimir_mensagem()

# Construtor de classe __init__()

class FuncionarioTecnico:
    def __init__(self, status):
        self.status = status

nivel = 'Técnico'
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')

print(nivel)  # Corrigido para imprimir o valor da variável nivel
print(func1.status)
print(func2.status)