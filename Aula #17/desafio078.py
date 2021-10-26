print('Desafio 78 - Maior e Menor valores na lista')
print('Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. \nNo final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. ')
print('')
valores = []
menor = maior = 0
cont = 0
for cont in range(1, 6):
    valores.append(int(input('Digite um valor: ')))
menor = min(valores)
maior = max(valores)
print('')
print(f'O menor valor é {menor} e está na(s) posição(s)', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')
print('')
print(f'O maior valor é {maior} e está na(s) posição(s)', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
