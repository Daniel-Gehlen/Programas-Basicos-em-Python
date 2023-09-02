``` mermaid
flowchart TD
  importSQLAlchemy[import sqlalchemy]
  importDeclarativeBase[import declarative_base]
  importSessionmaker[import sessionmaker]
  definirConexao[engine = create_engine 'sqlite:///exemplo_orm.db', echo=True]
  criarClasse[Base = declarative_base]
  criarTabela[Criar classe Aluno]
  criarCampos[Definir campos da tabela]
  criarTabelaBanco[Base.metadata.create_all engine]
  criarSessao[Session = sessionmaker bind=engine]
  criarSessaoInteracao[session = Session]
  inserirAluno[novo_aluno = Aluno nome='David', idade=23]
  adicionarAluno[session.add novo_aluno]
  commitTransacao[session.commit]
  consultarAlunos[alunos = session.query Aluno.all]
  imprimirDados[Imprimir dados retornados]
  fecharSessao[session.close]

  importSQLAlchemy --> definirConexao
  importDeclarativeBase --> criarClasse
  criarClasse --> criarCampos
  criarCampos --> criarTabela
  criarTabela --> criarTabelaBanco
  criarTabelaBanco --> criarSessao
  importSessionmaker --> criarSessao
  criarSessao --> criarSessaoInteracao
  criarSessaoInteracao --> inserirAluno
  inserirAluno --> adicionarAluno
  adicionarAluno --> commitTransacao
  commitTransacao --> consultarAlunos
  consultarAlunos --> imprimirDados
  imprimirDados --> fecharSessao


```