altura = []
idade = []

for i in range(5):
    a = float(input("Digite o valor da altura dos alunos:"))
    i = float(input("Digite o valor da idade dos alunos:"))
    media = len(a)/a
    altura.append(a)
    idade.append(i)
    if a > 13 and i > media:
        print(altura)
    else:
        print("fsdfas")