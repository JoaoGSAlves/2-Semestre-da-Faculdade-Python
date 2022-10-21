# Dupla: João Gabriel Alves, Leonardo Spitz

# Questão 1
# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida,
# calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
         "julho", "agosto", "setembro", "outubro", "novembro", "dezembro", ]
temperaturas = []

for i in range(12):
    temperaturas.append(
        float(
            input(f"Digite a temperatura do mês de {meses[i]} em graus celsius(°C): "))
    )
media = sum(temperaturas) / 12
print(f"\nA média das temperaturas foi {media:.2f}°C")
print("Meses com temperaturas acima da média: ")
for i in range(12):
    if temperaturas[i] > media:
        print(f"{i+1} - {meses[i].capitalize()} com {temperaturas[i]:.2f}ºC")

# Questão 2
# Implemente uma função recursiva para calcular 1 + 1/2 + 1/3 + 1/4 + ... + 1/N .


def frac(n):
    if (n == 1):
        return 1
    else:
        return 1/n + frac(n-1)


print(frac(4))

# Questão 3
# Implemente uma função recursiva para verificar se uma palavra é palíndromo
# (Ex. aba, abcba, xyzzyx).


def palindromo(palavra):
    if len(palavra) < 2:
        return ("É palindromo")
    if palavra[0] != palavra[-1]:
        return ("Não é palindromo")
    return palindromo(palavra[1:-1])


print(palindromo("arara"))
print(palindromo("arroz"))
print(palindromo("feijão"))
print(palindromo("reviver"))

# Questão 4
# Implemente uma lista circular com estrutura encadeada com os seguintes métodos:
# inserção, remoção e busca.


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None


class ListaCircular:
    def __init__(self):
        self.tail = None

    def lista_esta_vazia(self):
        return not self.tail

    # Função para Inserir
    def adicionar_na_frente(self, novo_nodo):
        if self.lista_esta_vazia():
            self.tail = novo_nodo
            novo_nodo.next = novo_nodo
        else:
            novo_nodo.next = self.tail.next
            self.tail.next = novo_nodo

    # Função para Remover
    def remover_ultimo(self):
        if self.lista_esta_vazia():
            print("Lista está vazia")
            return
        if self.tail.next == self.tail:
            self.tail.next = None
            self.tail = None
            return

        ultimo_nodo = self.tail
        ultimo_nodo = ultimo_nodo.next
        while ultimo_nodo.next != ultimo_nodo:
            ultimo_nodo = ultimo_nodo.next

        ultimo_nodo.next = ultimo_nodo.next
        self.tail = ultimo_nodo
        ultimo_nodo.next = None

    # Função para buscar
    def __str__(self):
        if self.tail == None:
            return "Lista Vazia"

        minha_lista = ""
        ultimo_nodo = self.tail
        atual = self.tail.next

        while True:
            minha_lista += f"{atual.valor} ->"
            if atual == ultimo_nodo:
                break
            atual = atual.next
        minha_lista += "None"

        return minha_lista


if __name__ == '__main__':
    minha_lista = ListaCircular()

minha_lista.adicionar_na_frente(Node(5))
minha_lista.adicionar_na_frente(Node(4))
minha_lista.adicionar_na_frente(Node(3))
minha_lista.adicionar_na_frente(Node(2))
minha_lista.adicionar_na_frente(Node(1))
print(minha_lista)
