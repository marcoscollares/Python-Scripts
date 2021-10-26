#COPIAR NO CADERNO
print('\033[1;4mDesafio 61 - Progressão Aritmética v2.0\033[m')
print('\033[1mRefaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.\033[m')

print('\033[1;34m=\033[m'*35)
print('       \033[1;36mProgressão Aritmética\033[m')
print('\033[1;34m=\033[m'*35)
a1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = a1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')

'''an = a1 + (10) * razão
print('A PA de {} na razão {} é: '.format(a1, razão))
while not a1 == an:
    print('{}'.format(a1), end=' -> ')
    a1 += razão
print('FIM')'''
