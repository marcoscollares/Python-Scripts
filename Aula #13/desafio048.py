print('\033[1;4mDesafio 48 - Soma Ímpares Multiplos de Três\033[m')
print('\033[1mFaça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.\033[m')

soma = 0
tot = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
          soma += c
          tot += 1
print('A soma de todos os \033[1;35m{}\033[m números ímpares é \033[1;36m{}\033[m.'.format(tot, soma))

#Outro modo de fazer
#for c in range(1, 500):
#    if c % 3 == 0 and c % 2 == 1:
#          soma += c
#          tot += 1
#print('A soma de todos os \033[1;35m{}\033[m números ímpares é \033[1;36m{}\033[m.'.format(tot, soma))