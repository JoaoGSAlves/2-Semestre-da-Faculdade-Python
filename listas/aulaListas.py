animais = ['gato','cao','pato','macaco']
print(animais)
# print(animais[0])
# print(animais[1])
# print(animais[2])
# print(animais[3])
# print(animais[-1 ])

#Função sum

notas = [0,10.0,7.0,6.0,8.0,9.0,]
# print ('\nA soma das notas e:', sum(notas))

#Função insert
notas.insert(1,5.0)
print('\n+','-='*20,'+')
print(notas)
print (len(notas))

#Função remove
notas.remove(0)
print(notas)

#Funções max e min
# print('\nA maior nota e:', max(notas))
# print('A menor nota e:', min(notas))

#Funções sort() e sorted()
notas.sort()
print(notas)
print('\n+','-='*20,'+')
print(sorted(animais)) 

# Função append
notas.append(3.5)
print('\n',notas)

# Função extend
notas.extend(animais)
print(notas) 