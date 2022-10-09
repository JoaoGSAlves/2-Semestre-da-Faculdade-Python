class Bola():
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocarCor(self, cor):
        self.cor = cor
    def mostraCor(self):
        return self.cor

p = Bola('verde',25,'borracha')
p2 = Bola('azul',25,'couro')
print(p.mostraCor())
p.trocarCor('azul')
print(p2.mostraCor())
print(p.mostraCor())