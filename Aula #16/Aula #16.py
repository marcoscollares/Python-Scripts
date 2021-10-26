lanche = ('Hambúrger', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(lanche)
print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3:])

#----------------------------------------

#lanche[1] = ('Refrigerante')
#print(lanche[1])

#----------------------------------------

#for comida in lanche:
#    print(f'Eu vou comer {comida}')
#print('Comi pra caramba!')

#----------------------------------------

#print(len(lanche))

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

#----------------------------------------

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]}')
print('Comi pra caramba!')

#----------------------------------------

for pos, comida in enumerate(lanche):
    #print(f'Eu vou comer {comida} na posição {pos}')
    print(pos, comida)

#----------------------------------------

print(sorted(lanche))

#----------------------------------------

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
d = b + a
print(a)
print(b)
print(c)
print(d)
print(len(c))
print(c.count(5))
print(c.index(2)) #Pega a primeira ocorrência de posição
print(c.index(2, 1)) #Com deslocamento

#----------------------------------------

pessoa = ('Gustavo', 39, 'M', 99.88)
print(pessoa)