``` mermaid
flowchart TD
  importSQLAlchemy["import sqlalchemy"]
  importDeclarativeBase["import declarative_base"]
  importSessionmaker["import sessionmaker"]
  definirConexao["DATABASE_URL = \"sqlite:///books.db\""]
  criarConexao["engine = create_engine DATABASE_URL"]
  criarSessao["Session = sessionmaker bind=engine"]
  criarSessaoInteracao["session = Session()"]
  criarBase["Base = declarative_base()"]
  criarClasseAuthor["Criar classe Author"]
  criarCamposAuthor["Definir campos da classe Author"]
  criarClasseBook["Criar classe Book"]
  criarCamposBook["Definir campos da classe Book"]
  criarRelacionamento["Relacionar classes Author e Book"]
  criarTabelasBase["Base.metadata.create_all engine"]
  criarAutores["author1 = Author name='J.K. Rowling'\nauthor2 = Author name='George Orwell'"]
  criarLivro1["book1 = Book title='Harry Potter and the Sorcerer\'s Stone' author=author1"]
  criarLivro2["book2 = Book title='1984' author=author2"]
  adicionarDados["session.add_all [author1, author2, book1, book2]"]
  commitTransacao["session.commit()"]
  consultarAutores["autores_e_livros = session.query Author.all()"]
  imprimirAutores["Imprimir autores e seus livros"]
  consultarLivros["livros_e_autores = session.query Book.all()"]
  imprimirLivros["Imprimir livros e seus autores"]

  importSQLAlchemy --> definirConexao --> criarConexao --> criarSessao --> criarSessaoInteracao --> criarBase --> criarClasseAuthor --> criarCamposAuthor --> criarClasseBook --> criarCamposBook --> criarRelacionamento --> criarTabelasBase --> criarAutores --> criarLivro1 --> criarLivro2 --> adicionarDados --> commitTransacao --> consultarAutores --> imprimirAutores --> consultarLivros --> imprimirLivros
```