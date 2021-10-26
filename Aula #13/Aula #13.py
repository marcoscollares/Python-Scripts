print('Aula 13 - Estrutura de Repetição por for')
from time import sleep
for c in range(1,6):
    print('Oi')
    sleep(1)
print('FIM')

print('=' * 30)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for d in range(i, f+1, p):
    print(d)
    sleep(0.5)
print('FIM')

print('='*10)

s = 0
for e in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))