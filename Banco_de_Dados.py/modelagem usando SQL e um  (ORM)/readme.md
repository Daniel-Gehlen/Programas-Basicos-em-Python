from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Definindo a conexão com o banco de dados
DATABASE_URL = "sqlite:///books.db"  # Usando SQLite como exemplo
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Declarando a base para a criação das tabelas
Base = declarative_base()

# Definindo as classes dos modelos (tabelas)
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='books')

# Criando as tabelas no banco de dados
Base.metadata.create_all(engine)

# Inserindo dados de exemplo
author1 = Author(name='J.K. Rowling')
author2 = Author(name='George Orwell')

book1 = Book(title='Harry Potter and the Sorcerer\'s Stone', author=author1)
book2 = Book(title='1984', author=author2)

session.add_all([author1, author2, book1, book2])
session.commit()

# Consultas usando SQLAlchemy
# Consulta 1: Listar todos os autores e seus livros
authors_and_books = session.query(Author).all()
for author in authors_and_books:
    print(f"Author: {author.name}")
    for book in author.books:
        print(f"  Book: {book.title}")

# Consulta 2: Listar todos os livros e seus autores
books_and_authors = session.query(Book).all()
for book in books_and_authors:
    print(f"Book: {book.title}")
    print(f"  Author: {book.author.name}")


# Neste exemplo, estamos usando o SQLAlchemy para definir dois modelos (tabelas): Author e Book,
# com uma relação de um para muitos entre eles. O ORM cuida da criação do esquema do 
# banco de dados, inserção dos dados e construção das consultas de maneira mais abstrata.

# As consultas demonstradas listam todos os autores e seus livros, e todos os livros com seus 
# autores, ilustrando como o ORM facilita a obtenção dos dados de maneira mais intuitiva.

# Lembre-se de que o exemplo usa SQLite como banco de dados. Em uma aplicação real, você pode 
# usar um banco de dados mais robusto, como MySQL, PostgreSQL ou SQL Server, ajustando a URL 
# de conexão conforme necessário.