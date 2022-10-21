# Lista como Estrutura Encadeada
# 1 - Implemente a função remove utilizando a função busca.

# class ListaEncadeada:
#     def __init__(self):
#         self.cabeca = None

#     def __repr__(self):
#         return "[" + str(self.cabeca) + "]"

#     def busca(pilha, valor):
#         corrente = pilha.cabeca
#         while corrente and corrente.dado != valor:
#             corrente = corrente.proximo
#         return corrente

#     def remocao(self, valor):
#         assert self.cabeca, "Impossivel remover valor de pilha vazia"

#         if self.cabeca.dado == valor:
#             self.cabeca = self.cabeca.proximo
#         else:
#             anterior = None
#             corrente = self.cabeca
#             busca(pilha, valor)

#             if corrente:
#                 anterior.proximo = corrente.proximo
#             else:
#                 anterior.proximo = None

# 2-  Remova duplicatas de uma pilha ordenada. Suponha que lhe seja fornecida uma pilha encadeada armazenando
# números inteiros em ordem crescente. Sua tarefa é remover todos os elementos duplicados da pilha.
# Por exemplo, dada a pilha [0 → 1 → 1 → 5 → 7 → 10 → 10 → None],
# seu programa deve retornar a pilha [0 → 1 → 5 → 7 → 10 → None].

# def remove_repetidos(pilha):
#     l = []
#     for i in pilha:
#         if i not in l:
#             l.append(i)
#     l.sort()
#     return l

# pilha = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9]

# pilha = remove_repetidos(pilha)
# print (pilha)

# 3- Defina as funções inserção, remoção e busca como métodos da Classe Lista.

# class ListaEncadeada:
#     def __init__(self):
#         self.cabeca = None

#     def __repr__(self):
#         return "[" + str(self.cabeca) + "]"

#     # Inserção
#     def insere_depois(pilha, nodo_anterior, novo_dado):
#         assert nodo_anterior, "Nodo anterior precisa existir na pilha."
#         novo_nodo = NodoLista(novo_dado)
#         novo_nodo.proximo = nodo_anterior.proximo
#         nodo_anterior.proximo = novo_nodo

#     # Busca
#     def busca(pilha, valor):
#         corrente = pilha.cabeca
#         while corrente and corrente.dado != valor:
#             corrente = corrente.proximo
#         return corrente

#     # remoção
#     def remocao(self, valor):
#         assert self.cabeca, "Impossivel remover valor de pilha vazia"

#         if self.cabeca.dado == valor:
#             self.cabeca = self.cabeca.proximo
#         else:
#             anterior = None
#             corrente = self.cabeca
#             while corrente and corrente.dado != valor:
#                 anterior = corrente
#                 corrente = corrente.proximo

#             if corrente:
#                 anterior.proximo = corrente.proximo
#             else:
#                 anterior.proximo = None

# ------------------------------------------------------------------------------
# Pilha como Estrutura Encadeada
# 1 - Escrever uma função que receba como parâmetro uma pilha. A função deve retornar o maior elemento da pilha.

# pilha = [1, 1, 2, 4, 5]
# def retornar_maximo(pilha):
#     return max(pilha)

# print(retornar_maximo(pilha))

# 2 - Utilizando uma pilha resolver o exercício a seguir: Dada uma sequência contendo N (N >0) números reais,
# imprimi-la na ordem inversa.

# pilha = []
# while True:
#     i = int(input('Digite um número: '))
#     if i < 1:
#         break
#     pilha.append(i)
# for i in pilha[::-1]:
#     print(i)

# 3- Escreva uma função que receba como parâmetro duas pilhas e verifique de elas são iguais.
# Duas pilhas são iguais se possuem os mesmos elementos, na mesma ordem.

# test_pilha1 = [1, 2, 4, 3, 5]
# teste_pilha2 = [1, 2, 4, 3, 5]
# print("A primeira pilha é : " + str(test_pilha1))
# print("A segunda pilha é : " + str(teste_pilha2))
# test_pilha1.sort()
# teste_pilha2.sort()
# if test_pilha1 == teste_pilha2:
#     print("As pilhas são idênticas")
# else:
#     print("As pilhas não são idênticas")

# 4 - Construa um programa utilizando uma pilha que resolva o seguinte problema:
# Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita.
# Dado uma placa verifique se o carro está estacionado na rua.
# Caso esteja, informe a sequência de carros que deverá ser retirada para que o carro em questão consiga sair.

# 5 - Implemente uma função chamada TPilha, que receba um vetor de inteiros com 15 elementos. Para cada um deles,
# como segue:
# Se o número for par, insira-o na pilha;
# Se o número lido for ímpar, retire um número da pilha;
# Ao final, esvazie a pilha imprimindo os elementos.


# pilha1 = []
# for i in range(5):
#     num = int(input("Escreva um número :"))
#     pilha1.append(num)

# print(pilha1)

# def Tpilha(valor):
#     new_pilha = []
#     for i in valor:
#         if i % 2 == 0:
#             new_pilha.append(i)
#         else:
#             new_pilha[::-1]

#     return new_pilha

# print(Tpilha(pilha1))

# Questão 6
# Escreva uma função chamada TPilha2 que recebe como parâmetro 2 pilhas (N e P) e um vetor de inteiros.
# Para cada um:
# se positivo, inserir na pilha P;
# se negativo, inserir na pilha N;
# se zero, retirar um elemento de cada pilha.


# pilha1 = []
# for i in range(5):
#     num = int(input("Escreva um número :"))
#     pilha1.append(num)

# print(pilha1)


# def Tpilha2(valor):
#     new_pilha_positive = []
#     new_pilha_negative = []
#     for i in valor:
#         if i > 0:
#             new_pilha_positive.append(i)
#         elif i == 0:
#             new_pilha_negative[::-1]
#             new_pilha_positive[::-1]
#         else:
#             new_pilha_negative.append(i)

#     return new_pilha_positive, new_pilha_negative


# print(Tpilha2(pilha1))

# Fila como Estrutura Encadeada
# Questão 1. Implemente uma fila dinâmica contendo todas as funcionalidades de uma fila padrão.
# –Crie um nó padrão da fila.
# –Crie uma função de inicialização da fila vazia
# –Crie uma função push que cria e insere um novo nó para o final da fila.
# –Crie uma função pop que remove o primeiro elemento da fila.


# # –Crie um nó padrão da fila.
# class Node:
#     def __init__(self, valor):
#         self.valor = valor
#         self.next = None

#     # –Crie uma função de inicialização da fila vazia


# class Fila:
#     def __init__(self):
#         self.tail = None

#     def lista_esta_vazia(self):
#         return not self.tail

#     # –Crie uma função push que cria e insere um novo nó para o final da fila.
#     def adicionar_no_final(self, novo_nodo):
#         if self.lista_esta_vazia():
#             self.tail = novo_nodo
#             novo_nodo.next = novo_nodo
#         else:
#             novo_nodo.next = self.tail.next
#             self.tail.next = novo_nodo
#             self.tail = novo_nodo
#     # –Crie uma função pop que remove o primeiro elemento da fila.

#     def remover_primeiro(self):
#         if self.lista_esta_vazia():
#             print("Lista está vazia")
#             return

#         if self.tail.next == self.tail:
#             self.tail.next = None
#             self.tail = None
#             return

#         primeiro_nodo = self.tail.next
#         segundo_nodo = primeiro_nodo.next
#         self.tail.next = segundo_nodo

# Questão 2 - Crie uma função de busca em que o usuário insere um valor (inteiro) e
# o programa retorna a sua posição na fila.

# Questão 3. Crie uma função que percorre e imprime todos os elementos da fila.
# Questão 4. Escreva uma função que inverta a ordem dos elementos da fila.  Por exemplo:
# [1] [4] [5] [2] → [2] [5] [4] [1]

# def __str__(self):
#     if self.tail == None:
#         return "Lista Vazia"

#     minha_lista = ""
#     ultimo_nodo = self.tail
#     atual = self.tail.next

#     while True:
#         minha_lista += f"{atual.valor} ->"
#         if atual == ultimo_nodo:
#             break
#         atual = atual.next
#     minha_lista += "None"

#     return minha_lista
#
# # def imprimir_inverso(self):
#     minha_lista.reverse()

#     return minha_lista
