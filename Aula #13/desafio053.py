print('\033[1;4mDesafio 53 - Detector de Palíndromo\033[m')
print('\033[1mCrie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.\033[m')

print('\033[1;35m-=\033[m'*15)
print('   \033[1;36mDETECTOR DE PALÍNDROMOS\033[m')
print('\033[1;35m=-\033[m'*15)

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de \033[1;33m{}\033[m é \033[1;37m{}\033[m.'.format(junto, inverso))
if inverso == junto:
    print('Temos um \033[1;34mpalíndromo\033[m!')
else:
    print('A frase digitada \033[1;31mnao é um palíndromo\033[m!')

#===============================================

#Outra forma de fazer o exercício de forma mais simplificada

#frase = str(input('Digite uma frase: ')).strip().upper()
#string = frase[::-1]
#print('O inverso de {} é {}.'.format(frase, string))
#if frase == string:
#    print('Portanto, a frase é um PALÍNDROMO!')
#else:
#    print('Portanto, a frase NÃO é um PALÍNDROMO!')