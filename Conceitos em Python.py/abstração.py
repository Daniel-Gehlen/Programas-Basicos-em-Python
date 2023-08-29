class Usuario:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3:
            self.livros_emprestados.append(livro)
            livro.emprestado_para = self
            print(f"{self.nome} emprestou '{livro.titulo}'.")
        else:
            print(f"{self.nome}, você atingiu o limite máximo de livros emprestados.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.emprestado_para = None
            print(f"{self.nome} devolveu '{livro.titulo}'.")
        else:
            print(f"{self.nome}, você não emprestou este livro.")

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado_para = None

# Criando objetos
usuario1 = Usuario("João", 25, "joao@email.com")
usuario2 = Usuario("Maria", 30, "maria@email.com")
livro1 = Livro("Aventuras Fantásticas", "Carlos Autor")
livro2 = Livro("O Mistério do Enigma", "Ana Escritora")

# Emprestando e devolvendo livros
usuario1.emprestar_livro(livro1)
usuario2.emprestar_livro(livro2)
usuario1.devolver_livro(livro2)

# Imagine que estamos desenvolvendo um sistema para uma biblioteca, e queremos criar uma abstração
# para os livros emprestados por usuários. Vamos criar classes que abstraem os conceitos relevantes
# e ocultam detalhes desnecessários.

# Nesse exemplo, usamos abstração para criar as classes Usuario e Livro, que representam conceitos
# do mundo real. A classe Usuario abstrai detalhes como o nome, idade e livros emprestados, 
# fornecendo métodos para emprestar e devolver livros. A classe Livro abstrai detalhes sobre o 
# título, autor e se está emprestado ou não.

# Essa abstração simplifica a interação com os objetos. Os detalhes de como os livros 
# são emprestados e devolvidos são encapsulados nos métodos das classes, permitindo que 
# os desenvolvedores interajam com esses objetos de forma mais intuitiva, sem se preocupar com
# implementações internas complexas