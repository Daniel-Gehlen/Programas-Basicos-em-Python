from sqlite3.dbapi2 import _Statement


class ClassName:
    _Statement-1
    _statement-N 
    

class PrimeiraClasse:
   nome = None

   def imprimir_mensagem(self):
      print('Ola seja bem vindo!')

objeto1 = PrimeiraClasse()
objeto1.nome = 'Aluno 1'

print(objeto1.nome)
objeto1.imprimir_mensagem()

#Construtor de classe __init__()

class FuncionarioTecnico:
   def __init__(self, status):
      self.status = status

nivel = 'Tecnico'
func1 = FuncionarioTecnico('Ativo')
func2 = FuncionarioTecnico('Licença Mestrado')

print(func1.nivel)
print(func2.nivel)
print(func1.status)
print(func2.status)
