#COPIAR NO CADERNO
print('Desafio 62 - Super Progressão Aritmética v3.0')
print('Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.')
print('='*35)
print('Super Progressão Aritmética')
print('='*35)

print('-'*40)
print('PROGRESSÃO ARITMÉTICA - MENU DE OPÇÕES')
print('-'*40)
a1 = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA: '))
termo = a1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(' {} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))


'''opcao = 0
a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
an = a1 + (10) * razao
print('A PA de {} na razão {} é:'.format(a1, razao))
while not a1 == an:
    print('{}'.format(a1), end=' => ')
    a1 += razao
print('FIM', end=' ')
menu = int(input('Você quer adicionar mais termos? Caso não, digite 0: '))
while not menu == 0:
    menu = int(input('Você quer adicionar mais termos? Caso não, digite 0: '))
    if menu != 0:
        an *= menu
        print('{}'.format(a1), end=' => ')
        a1 += razao


print('FIM')'''