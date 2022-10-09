# Exercício 1

# class Bola():
#     def __init__(self,cor,circunferencia,material):
#         self.cor = cor
#         self.circunferencia = circunferencia
#         self.material = material
    
#     def trocarCor(self, cor):
#         self.cor = cor
#     def mostraCor(self):
#         return self.cor

# p = Bola('verde',25,'borracha')
# p2 = Bola('azul',25,'couro')
# print(p.mostraCor())
# p.trocarCor('azul')
# print(p2.mostraCor())
# print(p.mostraCor())

# Exercício 2

# class Quadrado():
#     def __init__(self,lado):
#         self.lado = lado

#     def trocarLado(self,lado):
#         self.lado = lado

#     def mostrarLado(self):
#         return self.lado
    
#     def area(self):
#         return self.lado * self.lado

# q = Quadrado(5)
# print(q.mostrarLado())
# q.trocarLado(4)
# print(q.mostrarLado())
# print(q.area())

# Exercício 3

# class Retangulo():
#     def __init__(self,ladoA,ladoB):
#         self.ladoA = ladoA
#         self.ladoB = ladoB

#     def trocarLados(self,ladoA,ladoB):
#         self.ladoA = ladoA
#         self.ladoB = ladoB

#     def mostrarLado(self):
#         return self.ladoA, self.ladoB
    
#     def area(self):
#         return self.ladoA * self.ladoB

#     def perimetro(self):
#         return 2*(self.ladoA * self.ladoB)

# r = Retangulo(4,6)
# print(r.mostrarLado())
# print(r.area())
# print(r.perimetro())
# r.trocarLados(12,4)
# print(r.mostrarLado())
# print(r.perimetro())
# print(r.area())

# Exercício 4

# class Humano ():
#     def __init__(self,idade,peso,altura):
#         self.idade = idade
#         self.altura = altura
#         self.peso = peso

#     def mostrarAtributos(self):
#         return self.idade, self.altura, self.peso
    
#     def crescer(self,altura):
#         self.altura += altura

#     def envelhecer(self,anos):
#         for i in range(anos):
#             if self.idade < 21:
#                 self.crescer(0.5)
#             self.idade +=1

#     def engordar(self,peso):
#         self.peso += peso
#     def emagrecer(self,idade):
#         self.idade += idade

# h = Humano(12,32,145)
# print(h.mostrarAtributos())
# h.envelhecer(2)
# print(h.mostrarAtributos())
# h.crescer(2)
# print(h.mostrarAtributos())

# Exercício 5

# class contaBancaria():
#     def __init__(self,nome,saldo,numeroDaConta):
#         self.nome = nome
#         self.saldo = saldo
#         self.numeroDaConta = numeroDaConta
#     def alterarNome(self,nome):
#         self.nome = nome
#     def deposito(self,saldo):
#         self.saldo += saldo
#     def saque (self,saldo):
#         self.saldo -= saldo
#     def mostrarConta(self):
#         return self.nome,self.saldo,self.numeroDaConta

# c = contaBancaria('Waguinho',12000,45625)
# print(c.mostrarConta())
# c.deposito(50.0)
# print(c.mostrarConta())
# c.saque(4000)
# print(c.mostrarConta())

# Exercício 6

# class televisao():
#     def __init__(self,volume,canal):
#         self.volume = volume
#         self.canal = canal

#     def aumentarCanal(self,canal):
#         if self.canal + canal < 0:
#             self.canal = 0
#         elif self.canal + canal >500:
#             self.canal = 500
#         else:
#             self.canal += canal

#     def diminuirCanal(self,canal):
#         if self.canal - canal < 0:
#             self.canal = 0
#         elif self.canal - canal >500:
#             self.canal = 500
#         else:
#             self.canal -= canal

#     def aumentarVolume(self,volume):
#         if self.volume + volume < 0:
#             self.volume = 0
#         elif self.volume + volume >500:
#             self.volume = 500
#         else:
#             self.volume += volume

#     def diminuirVolume(self,volume):
#         if self.volume - volume < 0:
#             self.volume = 0
#         elif self.volume - volume >500:
#             self.volume = 500
#         else:
#             self.volume -= volume

#     def mostrarInfo(self):
#         return self.volume,self.canal

# t = televisao(43,231)
# t.aumentarCanal(54)
# t.aumentarVolume(31)
# print(t.mostrarInfo())
# t.diminuirCanal(200)
# t.diminuirVolume(101)
# print(t.mostrarInfo())


# Exercício 7

# class tamagoshi ():
#     def __init__(self,nome,fome,saude,idade):
#         self.nome = nome
#         self.saude = saude
#         self.fome = fome
#         self.idade = idade
    
#     def alterarNome (self,nome):
#         self.nome = nome
#     def alterarIdade (self,idade):
#         self.idade = idade
#     def alterarFome (self,fome):
#         self.fome = fome
#     def alterarSaude (self,saude):
#         self.saude = saude
    
#     def status (self):
#         return ('Nome:',self.nome,'Saude',self.saude,'Idade',self.idade,'Fome:',self.fome,'Tedio',self.tedio)
    
#     def humor (self):
#         return self.fome * self.saude


# t = tamagoshi('Pink',45,80,3)
# print(t.status())
# print(t.humor())

# Exercício 8

# class Macaco():
#     def __init__(self,nome):
#         self.nome = nome
#         self.bucho = []
    
#     def comer (self,comida):
#         self.bucho.append(comida)

#     def verBucho(self):
#         print("Comida no Bucho e:" , self.bucho)

#     def digerir (self):
#         if (len(self.bucho)> 0):
#             self.bucho.pop(0)

# m1 = Macaco('mamaco')
# m2 = Macaco('mococo')

# m1.comer('banana')
# m1.comer('melancia')
# m1.comer('maracuja')
# m1.verBucho()
# m1.digerir()
# m1.verBucho()

# Exercício 9

# Exercício 10

# class bombaCombustivel ():
#     def __init__(self,tipoCombustivel,valorLitro,quantidadeCombustivel):
#         self.tipoCombustivel = tipoCombustivel
#         self.valorLitro = valorLitro
#         self.quantidadeCombustivel = quantidadeCombustivel

#     def alterarValor(self,valorLitro):
#         self.valorLitro = valorLitro
#     def alterarCombustivel(self,quantidadeCombustivel):
#         self.quantidadeCombustivel = quantidadeCombustivel
#     def alterarTipo(self,tipoCombustivel):
#         self.tipoCombustivel = tipoCombustivel
    
#     def abastecerPorLitro(self,litro):
#         qtd = self.quantidadeCombustivel + litro
#         litro = self.valorLitro * litro  
#         print('A quantidade de combustivel agora e', qtd,'litros.')
#         print('O valor de combustivel a pagar e', litro,'reas.')

#     def abastecerPorValor(self,valor):
#         valor = valor/self.valorLitro
#         qtd2 = valor+self.quantidadeCombustivel
#         print('O valor a ser abastecido e', valor ,'litros!')
#         print(' O total de gasolina apos o abastecimento e', qtd2, 'litros.')

# b = bombaCombustivel('Diesel',5,25)
# print(vars(b))

# b.abastecerPorLitro(25)
# b.abastecerPorValor(50)
        
# Exercício 11
 
# class carro():
#     def __init__(self,consumo):
#         self.consumo = consumo
#         self.nivelCombustivel = 0

#     def adicionarGasolina(self,adicionarGasolina):
#         self.nivelCombustivel += adicionarGasolina
#         print('Voce abasteceu ',adicionarGasolina,'litros de combustivel!')

#     def andar(self,distancia):
#         temp = distancia/self.consumo
#         print('Voce andou',temp,'quilometros.')
#         self.nivelCombustivel -= temp

#     def verificarGasolina(self):
#         return self.nivelCombustivel

# c=carro(15)

# c.adicionarGasolina(20)
# c.andar(100)
# print(vars(c))
# print(c.verificarGasolina())

# Exercício 12

# class conta():
#     def __init__(self,saldo,taxaJuros):
#         self.saldo = saldo
#         self.taxaJuros = taxaJuros

#     def deposito(self,depositar):
#         self.saldo = self.saldo+depositar
#     def saque(self,sacar):
#         self.saldo = self.saldo-sacar
    
#     def verSaldo(self):
#         print('Seu saldo e:',self.saldo)
    
#     def juros(self):
#         self.saldo = self.saldo*self.taxaJuros


# c = conta(1000,1.1)
# print(vars(c))
# c.deposito(2000)
# c.verSaldo()
# c.saque(2000)
# c.verSaldo()
# c.juros()
# c.juros()
# c.juros()
# c.juros()
# c.juros()
# c.verSaldo()

#Exercício 13

# class funcionario():
#     def __init__(self,empregado,salario):
#         self.empregado = empregado
#         self.salario = salario

#     def getEmpregado(self):
#         return self.empregado
#     def getSalario(self):
#         return self.salario
    
# func = funcionario('Luiz',2050)
# print(vars(func))
# print('Nome:',func.getEmpregado(),'\nSalario:', func.getSalario())

#Exercício 14

# class funcionario():
#     def __init__(self,empregado,salario):
#         self.empregado = empregado
#         self.salario = salario

#     def getEmpregado(self):
#         return self.empregado
#     def getSalario(self):
#         return self.salario
    
#     def aumentaSalario(self,porcentagem):
#         self.salario = self.salario*(porcentagem/100+1)

# func = funcionario('Luiz',2050)
# print(vars(func))
# print('Nome:',func.getEmpregado(),'\nSalario:', func.getSalario())
# val = int(input('Digite o valor da porcentagem de seu aumento:'))
# func.aumentaSalario(val)
# print('Seu salario apos o aumento e: ', func.getSalario())

#Exercício 15

# class tamagoshi ():
#     def __init__(self,nome,fome,saude,idade,tedio):
#         self.nome = nome
#         self.saude = saude
#         self.fome = fome
#         self.idade = idade
#         self.tedio = tedio
    
#     def getNome (self):
#         return self.nome
#     def getIdade (self):
#         return self.idade
#     def getFome (self):
#         return self.fome
#     def getSaude (self):
#         return self.saude
    
#     def setNome (self,nome):
#         self.nome = nome  
#     def setIdade (self,idade):
#         self.idade = idade
#     def setFome (self,fome):
#         self.fome = fome
#     def setSaude (self,saude):
#         self.saude = saude
    
#     def alimentar(self,qtde):
#         if (qtde > 0) and (qtde <100):
#             self.fome = self.fome - qtde
            
#     def brincar(self,exercicio):
#         if (exercicio > 0) and (exercicio <100):
#             self.saude = self.saude + exercicio
#             self.tedio = self.tedio - exercicio

#     def status (self):
#         return ('Nome:',self.nome,'Saude',self.saude,'Idade',self.idade,'Fome:',self.fome,'Tedio',self.tedio)
#     def humor (self):
#         return self.fome * self.saude

# t = tamagoshi('Pink',45,80,3,82)
# print(vars(t))
# print('O humor do tamagoshi e:', t.humor())
# t.alimentar(23)
# print(vars(t))
# t.brincar(67)
# print(vars(t))

#Exercício 16

# class tamagoshi ():
#     def __init__(self,nome,fome,saude,idade,tedio):
#         self.nome = nome
#         self.saude = saude
#         self.fome = fome
#         self.idade = idade
#         self.tedio = tedio
    
#     def getNome (self):
#         return self.nome
#     def getIdade (self):
#         return self.idade
#     def getFome (self):
#         return self.fome
#     def getSaude (self):
#         return self.saude
    
#     def setNome (self,nome):
#         self.nome = nome  
#     def setIdade (self,idade):
#         self.idade = idade
#     def setFome (self,fome):
#         self.fome = fome
#     def setSaude (self,saude):
#         self.saude = saude
    
#     def alimentar(self,qtde):
#         if self.fome - qtde < 0:
#             self.fome = 0
#         else:
#             self.fome-= qtde      

#     def brincar(self,exercicio):
#         if (exercicio > 0) and (exercicio <100):
#             self.saude = self.saude + exercicio
#             self.tedio = self.tedio - exercicio

#     def status (self):
#         return ('Nome:',self.nome,'Saude',self.saude,'Idade',self.idade,'Fome:',self.fome,'Tedio',self.tedio)
#     def humor (self):
#         return self.fome * self.saude
    
# t = tamagoshi('Pink',45,80,3,82)
# print(t.status())
# print('O humor do tamagoshi e:', t.humor())
# t.alimentar(23)
# print(t.status())
# t.brincar(67)
# print(t.status())

#Exercício 17

# from random import randint 

# class tamagoshi ():
#     def __init__(self,nome,fome,saude,idade):
#         self.nome = nome
#         self.saude = saude
#         self.fome = fome
#         self.idade = idade
    
#     def getNome (self):
#         return self.nome
#     def getIdade (self):
#         return self.idade
#     def getFome (self):
#         return self.fome
#     def getSaude (self):
#         return self.saude
    
#     def setNome (self,nome):
#         self.nome = nome  
#     def setIdade (self,idade):
#         self.idade = idade
#     def setFome (self,fome):
#         self.fome = fome
#     def setSaude (self,saude):
#         self.saude = saude

#     def humor(self):
#         return self.getFome()*self.getSaude()
    
#     def alimentar(self,qtde):
#         if self.fome - qtde < 0:
#             self.fome = 0
#         else:
#             self.fome-= qtde      

#     def brincar(self,exercicio):
#         if (exercicio > 0) and (exercicio <100):
#             self.saude = self.saude + exercicio

#     def status (self):
#         return ('Nome:',self.nome,'Saude',self.saude,'Idade',self.idade,'Fome:',self.fome,'Tedio',self.tedio)
#     def humor (self):
#         return self.fome * self.saude


# a = tamagoshi('Godzila',randint(0,100),randint(0,100),4)
# b = tamagoshi('Dinossauro',randint(0,100),randint(0,100),6)
# c = tamagoshi('Fuleco',randint(0,100),randint(0,100),6)
# d = tamagoshi('Macaco',randint(0,100),randint(0,100),5)
# lista = []
# lista.append(a)
# lista.append(b)
# lista.append(c)
# lista.append(d)

# while True:
#     print(":::: FAZENDA ::::")
#     print("1. Alimentar todos os tamagoshis")
#     print("2. Brincar com todos os tamagoshis")
#     print("3. Ouvir todos os tamagoshis")
#     print("4. Sair")
#     op = int(input())

#     if (op == 1):
#         alimento = int(input("Alimentar todos com: "))
#         for i in range(3):
#             lista[i].alimentar(alimento)

#     elif(op ==2):
#         brinquedo = int(input("Brincar todos com: "))
#         for i in range(3):
#             lista[i].brincar(brinquedo)

#     elif(op == 3):
#         for i in range(3):
#            print(lista[i].getNome() + ": " + str(lista[i].humor()))

#     elif(op == 4):
#         break