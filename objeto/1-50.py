# Exercício 1
# nota=float(input("informe um numero de 0 a 10: "))
# while (nota>10) or (nota<0):
# 	nota=float(input("informe um numero de 0 a 10: "))

# Exercício 2
# x = str(input('Digite o nome de Usuário:'))
# y = str(input('Digite sua senha:'))
# while x == y:
#     print('Digite um usuário diferente da senha!')
#     x = str(input('Digite o nome de Usuário:'))
#     y = str(input('Digite sua senha:'))

# Exercicío 3
# nome = str(input("Digite um nome: "))
# while (len(nome) <= 3):
#     nome = str(input("Digite um nome: "))
# idade = int(input("Digite a idade: "))
# while (idade > 150 or idade < 0):
#     idade = int(input("Digite a idade: "))
# salario = float(input("Informe um salário: "))
# while (salario < 0):
#     salario = float(input("Informe um salário: "))
# sexo = str(input("Digite a inicial do seu sexo: "))
# while sexo != "f" and sexo != "m":
#     sexo = str(input("Digite a inicial do seu sexo: "))
# estado_civil = str(input("Digite a inicial do seu estado civil:"))
# while (estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d"):
#     estado_civil = str(input("Digite a inicial do seu estado civil:"))

# Exercicío 4
# anos= 0
# A= 80000
# B= 200000
# while A <= B:
#     A += A * 0.03
#     B += B * 0.015
#     anos += 1
#
# print(' A cidade A ultrapassará, ou se igualará a cidade B em %.d anos: ' %anos)

# Exercício 5
# z= int(input('Para iniciar a operação digite 1 e para encerrar digite 2:'))
# while z!=0:
#     anos= 0
#     A= int(input('Digite o número total de habitantes de Cidade A:'))
#     B= int(input('Digite o número total de habitantes de Cidade B:'))
#     x = float(input('Digite o valor da taxa de crescimento da Cidade A:'))
#     y = float(input('Digite o valor da taxa de crescimento da Cidade B:'))
# 
#     while A <= B :
#         A += A * x
#         B += B * y
#         anos += 1
#     print(' \nA cidade A ultrapassará, ou se igualará a cidade B em %.d anos: ' %anos)
#     print('+-'*30)
#     z = int(input('\nPara iniciar outra operação digite um número diferente de 0'
#                   '\nPara encerrar o programa digite 0:'))

# Exercício 6

# for i in range(1,21):
#     print(i)


# print(list(range(1,21)))

# Exercício 7

# x = float(input("Número 1: "))
# y = float(input("Número 2: "))
# z = float(input("Número 3: "))
# w = float(input("Número 4: "))
# v = float(input("Número 5: "))

# lista = [x, y, z, w, v]

# print("O maior número é: ", max(lista))

# Exercício 8

# x = float(input("Número 1: "))
# y = float(input("Número 2: "))
# z = float(input("Número 3: "))
# w = float(input("Número 4: "))
# v = float(input("Número 5: "))

# soma = x + y + z + w + v
# media = soma / 5

# print("Soma: ", soma, "\nMedia: ", media)

# Exercicío 9  

# for i in range(3, 50, 2):
#     print(i)

# Exercício 10

# x = int(input("Digite um número: "))
# y = int(input("Digite outro número: "))

# for i in range(x + 1, y):
#         print(i)
# for i in range(y + 1, x):
#         print(i)

# Exercício 11

# x = int(input("Digite um número: "))
# y = int(input("Digite outro número: "))

# for i in range(x + 1, y):
#         print(i)
# for i in range(y + 1, x):
#         print(i)

# Exercício 12

# n = int(input("digite um numero de 1 a 10: "))
# cont = 1

# while cont <= 10:
#     tab = n * cont
#     print(n, "X", cont, "=", tab)
#     cont = cont + 1

# Exercício 13

# base = int(input("Digite a base: "))
# expoente = int(input("Digite expoente: "))
# resultado = 1

# for i in range(expoente):
#     resultado = base * base
#     resultado = base * resultado

# print(resultado)

# Exercício 14

# n1 = int(input("\nDigite o número: "))
# n2 = int(input("Digite o número: "))
# n3 = int(input("Digite o número: "))
# n4 = int(input("Digite o número: "))
# n5 = int(input("Digite o número: "))
# n6 = int(input("Digite o número: "))
# n7 = int(input("Digite o número: "))
# n8 = int(input("Digite o número: "))
# n9 = int(input("Digite o número: "))
# n10 = int(input("Digite o número: "))
# list1 = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

# par = 0
# impar = 0

# for value in list1:
#     if value % 2 == 0:
#         par = par + 1
#     else:
#         impar = impar + 1

# print("Par: ", par, "\nImpar: ", impar)

# Exercício 15

# ultimo = 1
# penultimo = 1
# count = 1
# print(ultimo)
# print(penultimo)
# while count <= 9:
#         termo = ultimo + penultimo
#         penultimo = ultimo
#         ultimo = termo
#         count += 1
#         print(termo)

# Exercício 16

# ultimo = 1
# penultimo = 1
# print(ultimo)
# print(penultimo)
# termo = 0

# while termo < 500:
#     termo = ultimo + penultimo
#     penultimo = ultimo
#     ultimo = termo
#     if termo < 500:
#         print(termo)
#     else:
#         print("O proximo valor será maior que 500")

# Exercício 17

# numero = int(input("Digite um número: "))
# count1 = 0
# count = 1
# while count1 < numero:
#     fatorial = numero * (numero - count)
#     count = count - 1
#     count1 = count + 1

# print(fatorial)

# Exercício 18

# lista = []
# count = 0

# quant = int(input("Digite a quantiade de número que deseja digitar: "))
# while quant != count:
#     numero = lista.append(float(input("Digite um número: ")))
#     count += 1

# print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
# print("Soma: ", max(lista) + min(lista))

# Exercício 19


# lista = []
# count = 0

# quant = int(input("Digite a quantiade de número que deseja digitar: "))
# while quant != count:
#     numero = float(input("Digite um número: "))

#     while numero > 1000 or numero < 0:
#         numero = float(input("Digite um número[erro]: "))
        
#     lista.append(numero)
#     count += 1

# print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
# print("Soma: ", max(lista) + min(lista))

# Exercício 20

# import math
# lista = []
# count = 0

# quant = int(input("Digite a quantiade de número que deseja digitar: "))
# while quant != count:
#     numero = float(input("Digite um número: "))
#     while numero // 1 != numero or numero < 0 or 0 or numero < 16:
#         numero = float(input("Digite um número[erro]: "))

#     print("Fatorial do número digitado: ", math.factorial(numero))
#     count += 1

# Exercício 21

# numero = int(input("\nDigite um número: "))

# if numero % 2 == 0 and numero != 2:
#     print("não primo")
# else:
#     print("primo")

# Exercício 22

# numero = int(input("\nDigite um número: "))
# lista = []


# if numero % 2 != 0 or numero == 2:
#     print("primo")
# else:
#     for i in range(numero):
#         if numero % (i + 1) == 0:

#             lista.append(i + 1)

# print("Os números divisiveis por ", numero, " são ", lista)

# Exercício 23

# numero = int(input("\nDigite um número: "))
# lista = []
# divisoes = 0

# for i in range(numero + 1):
#     if i % 2 == 1 and i != 2:
#         lista.append(i)
#         divisoes += 1
#     else:
#         divisoes += 1
# print("Números primos: ", lista)
# print("Número de divisões", divisoes)

# Exercício 24

# numero_notas = int(input("Digite o número de notas que você irá digitar: "))
# count = 0
# todas_notas = []

# while count < numero_notas:
#     notas = todas_notas.append(float(input("Digite a nota: ")))
#     count += 1

# media = sum(todas_notas) / numero_notas
# print("A média é igual a ", media)

# Exercício 25

# n_pessoas = int(input("Digite o número de pessoas que ira digitar a idade: "))
# lista = []

# for i in range(n_pessoas):
#     idade = lista.append(int(input("Digite a idade: ")))


# if sum(lista) / len(lista) < 25:
#     print("jovem")
# elif sum(lista) / len(lista) >= 25 and sum(lista) / len(lista) < 60:
#     print("adulto")
# else:
#     print("idosa")

# Exercício 26

# eleitores = int(input("Digite o número de eleitores: "))
# votos = []

# for i in range(eleitores):
#     voto = votos.append(int(input("Qual candidato deseja votar? [1, 2, 3]: ")))

# print("Quantidade de votos para candidato 1: ", votos.count(1))
# print("Quantidade de votos para candidato 2: ", votos.count(2))
# print("Quantidade de votos para candidato 3: ", votos.count(3))

# Exercício 27

# turmas = int(input("Quantas turmas? : "))
# alunos_turmas = []
# turma = 1

# for i in range(turmas):
#     print("turma ", turma)
#     alunos = int(input("Alunos da turma : "))
#     while alunos > 40:
#         print("turma ", turma, " [uma turma só pode ter 40 alunos]")
#         alunos = int(input("Alunos da turma : "))
#     turma += 1
#     alunos_turmas.append(alunos)

# media = sum(alunos_turmas) / len(alunos_turmas)
# print("A media e igual a: ", media)

# Exercício 28

# quant_cds = int(input("Digite a quantidade de CD's : "))
# cds = []
# n_cd = 1

# for i in range(quant_cds):
#     print("CD número ", n_cd)
#     valor_cd = cds.append(float(input("Digite o valor do CD: ")))
#     n_cd += 1

# media = sum(cds) / len(cds)
# print("A media para cada CD é: ", media)

# Exercício 29

# produtos = int(input("Digite a quantidade de produtos: "))
# while produtos > 50:
#     produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))


# precos = []
# n_produto = 1
# count = 0

# for i in range(produtos):
#     print("Produto N° ", n_produto)
#     preco = precos.append(float(input("Digite o preco do produto: ")))
#     n_produto += 1

# n_produto = 1
# for j in range(produtos):
#     print("Produto N° ", n_produto, "= ", precos[count])
#     count += 1
#     n_produto += 1

# Exercício 30

# paes = int(input("Digite a quantidade de pães: "))
# while paes > 50:
#     produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

# count = 1
# preco_pao = float(input("Qual é o preço do pão? : "))

# for j in range(paes):
#     print(count, "= R$", round(preco_pao * count, 2))
#     count += 1

# Exercício 31

# import time

# while True:
#     precos_produtos = []
#     preco_produto = True
#     n_produto = 1

#     while preco_produto != 0:
#         print("Produto n° ", n_produto)
#         preco_produto = float(input("Digite o preço do produto: "))
#         precos_produtos.append(preco_produto)
#         n_produto += 1

#     print("Total: ", sum(precos_produtos))
#     dinheiro = float(input("Digite a quantida que irá pagar: "))

#     while dinheiro < sum(precos_produtos):
#         dinheiro = float(input("Digite a quantida que irá pagar[maior que o total da compra] : "))

#     print("Dinheiro: R$", dinheiro)
#     print("Troco: R$", dinheiro - sum(precos_produtos))
#     print("\nPróxima compra em 3 segundos...")
#     time.sleep(3)
#     print("\n" * 5)

# Exercício 32

# import math
# numero = int(input("\nDigite o numero que quer realizar a fatorial : "))
# count = numero
# fatorial = math.factorial(numero)

# for i in range(numero - 1):
#     print(count, end=" * ")
#     count -= 1
# print("1 = ", fatorial)

# # Exercício 33

# n_temperaturas = int(input("Quantidade de temperaturas que irá digitar: "))
# temperaturas = []
# n_temperatura = 1
# for i in range(n_temperaturas):
#     print("Temperatura n° ", n_temperatura)
#     temperatura = temperaturas.append(float(input("Digite a temperatura: ")))
#     n_temperatura += 1

# print("Maior temperatura = ", max(temperaturas))
# print("Menor temperatura = ", min(temperaturas))
# print("Média = ", round(sum(temperaturas) / len(temperaturas), 2))

# # Exercício 34

# numero = int(input("\nDigite um número: "))

# if numero % 2 == 0 and numero != 2:
#     print("não primo")
# else:
#     print("primo")


# # Exercício 35

# numero = int(input("\nDigite um número: "))
# lista = []

# for i in range(numero + 1):
#     if i % 2 == 1 and i != 2:
#         lista.append(i)

# print("Números primos: ", lista)

# # Exercício 36

# n_tabuada = int(input("\nDigite o número para fazer a tabuada: "))
# n_inicial = int(input("Iniciar a tabuada no : "))
# n_final = int(input("Finalizar a tabuada no : "))

# caminho = n_inicial

# for i in range(n_inicial, n_final + 1):
#     print(n_tabuada, " X ", caminho, " = ", n_tabuada * caminho)
#     caminho += 1

# # Exercício 37

# cod_clientes = []
# altura_clientes = []
# peso_clientes = []
# n_cliente = 1
# codigo = True

# while codigo != 0:
#     print("\nCliente n° ", n_cliente)
#     codigo = int(input("Digite o código: "))
#     if codigo == 0:
#         break
#     else:
#         altura = float(input("Digite a altura: "))
#         peso = float(input("Digite o peso: "))
#         cod_clientes.append(codigo)
#         altura_clientes.append(altura)
#         peso_clientes.append(peso)
#         n_cliente += 1

# cod_magro = peso_clientes.index(min(peso_clientes))
# cod_gordo = peso_clientes.index(max(peso_clientes))
# cod_alto = altura_clientes.index(max(altura_clientes))
# cod_baixo = altura_clientes.index(min(altura_clientes))
# print("\n" * 5)
# print("Código do mais magro: ", cod_clientes[cod_magro])
# print("Código do mais gordo: ", cod_clientes[cod_gordo])
# print("Código do mais alto: ", cod_clientes[cod_alto])
# print("Código do mais baixo: ", cod_clientes[cod_baixo])
# print("Média de altura: ", sum(altura_clientes) / len(altura_clientes))
# print("Média de peso: ", sum(peso_clientes) / len(peso_clientes))

# # Exercício 38

# salario = float(input("Dgite o salario inicial do funcionario: "))
# aumento = 1.5

# for i in range(1996, 2018 + 1):
#     aumento = aumento * 2
#     salario_atual = salario + (salario * (aumento / 100))
#     print("Salario em ", i, " = ", salario_atual)

# # Exercício 39

# numero_alunos = []
# altura_alunos = []

# for i in range(10):
#     print("\nDigitação número ", i + 1," :")
#     n_aluno = int(input("Digite o número do aluno: "))
#     while n_aluno in numero_alunos:
#         print("[Este número ja foi digitado]")
#         n_aluno = int(input("Digite outro número: "))
#     a_aluno = altura_alunos.append(float(input("Digite a altura do aluno: ")))
#     numero_alunos.append(n_aluno)

# indice_baixo = altura_alunos.index(min(altura_alunos))
# indice_alto = altura_alunos.index(max(altura_alunos))

# print("Aluno mais baixo \nNúmero: ", numero_alunos[indice_baixo], "\nAltura: ", min(altura_alunos))
# print("Aluno mais alto \nNúmero: ", numero_alunos[indice_alto], "\nAltura: ", max(altura_alunos))

# # Exercício 40

cod_cidades = []
n_veiculos = []
n_acidentes = []
acidentes_2000 = []

for i in range(5):
    print("\nCidade número ", i + 1)
    codigo_cidade = int(input("Digite o código da cidade: "))
    while codigo_cidade in cod_cidades:
        print("[Código já digitado]")
        codigo_cidade = int(input("Digite outro código: "))

    numero_acidentes = int(input("Digite o número de acidentes: "))
    numero_veiculos = int(input("Digite o número de veiculos: "))

    if numero_veiculos > 2000:
        acidentes_2000.append(numero_acidentes)
        n_acidentes.append(numero_acidentes)
    else:
        n_acidentes.append(numero_acidentes)

    n_veiculos.append(numero_veiculos)
    cod_cidades.append(codigo_cidade)

indice_acidentes_menor = n_acidentes.index(min(n_acidentes))
indice_acidentes_maior = n_acidentes.index(max(n_acidentes))

print("\nMenos acidentes\nQuantidade de acidentes: ", min(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_menor])
print("\nMais acidentes\nQuantidade de acidentes: ", max(n_acidentes), "\nCódigo da cidade: ", cod_cidades[indice_acidentes_maior])

media_veiculos = sum(n_veiculos) / len(n_veiculos)
print("\nMédia de veiculos nas 5 cidades: ", media_veiculos)

media_acidentes_2000 = sum(acidentes_2000) / len(acidentes_2000)
print("\nMédia de acidentes nas cidades com menos de 2000 veículos: ", media_acidentes_2000)