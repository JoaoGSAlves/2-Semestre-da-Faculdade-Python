class Pessoa:
    def __init__(self,nome, peso):
        self.nome = nome
        self.peso = peso
        print('bua bua chorou o', self.nome)

    def rir(self) :
        print(self.nome,'kkkkk')

    def sorrir(self):
        print(':)')

    def comer(self,comida ):
        print(self.nome, 'Comendo meu lanche',comida)

# p1 = Pessoa('Bruno', 2)
# p2 = Pessoa('Daniele', 3) 
p3 = Pessoa('Ze', 4)
p3.rir(), p3.sorrir(), p3.comer('Arroz')
p3.nome = 'maluco'
p3.rir()

# p1.rir(), p1.sorrir(), p1.comer()
# p2.rir()
