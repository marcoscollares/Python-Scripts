print('\033[1;4mDesafio 51 - Progressão Aritmética\033[m')
print('\033[1mDesenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.\033[m')

print('\033[1;35m=\033[m'*35)
print('    \033[1;4;36mOs 10 Primeiros Termos da PA\033[m')
print('\033[1;35m=\033[m'*35)
a1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
an = a1 + (10 - 1) * razao
for PA in range(a1, an+1, razao):
    print(PA,end=' -> ')
print('FIM')