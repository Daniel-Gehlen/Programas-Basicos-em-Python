# Aqui está um exemplo de código em Python usando a biblioteca SQLAlchemy para realizar mapeamento
# objeto-relacional e recuperar dados de um banco de dados:

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definir a conexão com o banco de dados
engine = create_engine('sqlite:///exemplo_orm.db', echo=True)

# Criar uma classe que representa a tabela no banco de dados
Base = declarative_base()

class Aluno(Base):
    __tablename__ = 'alunos'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criar a tabela no banco de dados (caso não exista)
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Inserir um aluno na tabela
novo_aluno = Aluno(nome='David', idade=23)
session.add(novo_aluno)
session.commit()

# Consultar e retornar todos os alunos
alunos = session.query(Aluno).all()

# Imprimir os dados retornados
for aluno in alunos:
    print(f'ID: {aluno.id}, Nome: {aluno.nome}, Idade: {aluno.idade}')

# Fechar a sessão
session.close()

