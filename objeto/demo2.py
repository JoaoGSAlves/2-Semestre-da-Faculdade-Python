class Carro ():
    def __init__(self, chassi, nome):
        self.chassi = chassi
        self.nome =  nome

    def trocarChassi(self,chassi):
        self.chassi = chassi

    def trocarNome(self, nome):
        self.nome = nome
    
    def mostrarChassi(self):
        return self.chassi

    def mostrarNome(self):
        return self.nome

c = Carro ('XXY-335','Anderson')
print(c.mostrarNome())
print(c.mostrarChassi())
c.trocarNome('Michael')
print('O novo proprietario se chama:',c.mostrarNome())
c.trocarChassi('XYZ-934')
print('A nova placa e:',c.mostrarChassi())