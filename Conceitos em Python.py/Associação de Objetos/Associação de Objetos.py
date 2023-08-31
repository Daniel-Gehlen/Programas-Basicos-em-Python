# Vamos considerar um cenário onde temos duas classes: Author (Autor) e Book (Livro). 
#Um autor pode ter escrito vários livros, e um livro deve estar associado a um único autor. 
#Isso é um exemplo de uma relação de associação unidirecional onde a classe Author tem 
#uma associação com a classe Book.


class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year
        self.books = []  # Lista para armazenar os livros escritos pelo autor

    def add_book(self, book):
        self.books.append(book)

class Book:
    def __init__(self, title, year, author):
        self.title = title
        self.year = year
        self.author = author  # Referência ao autor do livro

# Criando instâncias de Author
author1 = Author("J.K. Rowling", 1965)
author2 = Author("George Orwell", 1903)

# Criando instâncias de Book e associando-as aos autores
book1 = Book("Harry Potter and the Sorcerer's Stone", 1997, author1)
book2 = Book("1984", 1949, author2)
book3 = Book("Animal Farm", 1945, author2)

# Associando os livros aos autores
author1.add_book(book1)
author2.add_book(book2)
author2.add_book(book3)

# Exemplo de acesso às informações
print(f"{author1.name} wrote {len(author1.books)} books.")
print(f"{author2.name} wrote {len(author2.books)} books.")
print(f"{book1.title} was written by {book1.author.name} in {book1.year}.")
print(f"{book2.title} was written by {book2.author.name} in {book2.year}.")


# Nesse exemplo, a classe Author possui uma lista chamada books que armazena as instâncias de 
# livros associadas a esse autor. A classe Book tem uma referência ao autor que escreveu o livro.

# Essa é uma forma simples de ilustrar associação entre objetos em programação orientada a objetos. 
# A classe Author "tem" uma lista de livros, e a classe Book "usa" uma instância de autor para 
# estabelecer a associação.