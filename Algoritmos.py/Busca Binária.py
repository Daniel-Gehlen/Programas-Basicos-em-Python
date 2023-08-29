# Algoritmo de busca binária

class Buscador:

    def busca_sequncial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista)-1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1
    
lista = [-200, 4, 50, 333]
print(lista)

b = Buscador()

print(b.busca_binaria(lista, 50))

# Explicação do código

# class Buscador:
# Nesta linha, você está definindo uma classe chamada "Buscador" que conterá os métodos para 
# realizar a busca sequencial e a busca binária.

    # def busca_sequncial(self, lista, x):
# Aqui, você está definindo o método de busca sequencial dentro da classe Buscador. 
# O método recebe dois parâmetros: "lista", que é a lista onde você deseja buscar o elemento,
# e "x", que é o elemento que você está buscando na lista.

        # for i in range(len(lista)):
        #     if lista[i] == x:
        #         return i
# Este trecho de código implementa a busca sequencial. Ele percorre cada elemento da lista
# usando um loop "for". Se o elemento atual (lista[i]) for igual ao elemento procurado (x), 
# a função retorna o índice onde o elemento foi encontrado (ou seja, o valor de "i").

#        return -1
# Caso nenhum elemento correspondente seja encontrado na lista, a função retorna -1 para indicar
# que o elemento não foi encontrado.

#     def busca_binaria(self, lista, x):
# Aqui, você está definindo o método de busca binária dentro da classe Buscador.
# Assim como antes, o método recebe a lista onde você deseja buscar ("lista") e o elemento que 
# está sendo procurado ("x").

        # primeiro = 0
        # ultimo = len(lista)-1
# Neste trecho, você está inicializando duas variáveis, "primeiro" e "ultimo", que serão
# utilizadas para acompanhar os índices iniciais e finais da parte da lista onde você está
# buscando.

        # while primeiro <= ultimo:
# Este é o início de um loop "while" que será executado enquanto o índice "primeiro" for menor 
# ou igual ao índice "ultimo". Isso significa que a busca será realizada enquanto 
# a parte da lista onde o elemento pode estar não se esgotar.

            # meio = (primeiro + ultimo)//2
# Nesta linha, você calcula o índice do elemento do meio da parte da lista atualmente 
# considerada. Isso é feito dividindo a soma dos índices "primeiro" e "ultimo" por 2. 
# Isso é fundamental para a busca binária, pois permite dividir a lista em duas partes e
# descartar uma delas a cada iteração.

            # if lista[meio] == x:
            #     return meio
# Aqui, você verifica se o elemento no índice "meio" da lista é igual ao elemento procurado ("x").
# Se for o caso, você retorna o índice "meio" como o índice onde o elemento foi encontrado.

            # else:
            #     if x < lista[meio]:
            #         ultimo = meio - 1
            #     else:
            #         primeiro = meio + 1
# Neste bloco de código, você está ajustando os índices "primeiro" e "ultimo" com base 
# na comparação entre o elemento procurado ("x") e o elemento no índice "meio". Se o elemento
# procurado for menor que o elemento no índice "meio", você atualiza o índice "ultimo" para 
# apontar para o elemento anterior ao índice "meio". Caso contrário, você atualiza o índice 
# "primeiro" para apontar para o elemento seguinte ao índice "meio".

        # return -1
# Se o loop "while" se esgotar e nenhum elemento correspondente for encontrado, a função retorna
# -1 para indicar que o elemento não foi encontrado.

        # lista = [-200, 4, 50, 333]
        # print(lista)

        # b = Buscador()
        # print(b.busca_binaria(lista, 50))
# Nestas últimas linhas, você cria uma lista chamada "lista" e a imprime. Em seguida, cria uma
# instância da classe "Buscador" chamada "b" e chama o método "busca_binaria" dessa instância
# para procurar o elemento 50 na lista. O resultado da busca binária é impresso, que será 
# o índice onde o elemento 50 foi encontrado, ou -1 se não foi encontrado.








