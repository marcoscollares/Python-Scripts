#COPIAR NO CADERNO
print('Desafio 65 - Maior e Menor Valores')
print('Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. \nO programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.')
resp = 'S'
soma = total = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    total += 1
    if total == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] '))
media = soma / total
print('Você digitou {} números e a média foi {}.'.format(total, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))





'''soma = cont = media = 0
menor = 0
maior = 0
resposta = 0
while not resposta == 'Nn':
    num = int(input('Digite um número inteiro: '))
    maior = num
    menor = num
    cont += 1
    soma += num
    resposta = str(input('Você deseja continuar a digitar mais valores? [S/N]: ')).strip().upper()[0]
    if resposta == 'Ss':
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / total
print('A média dos valores digitados é {}. O menor valor é {}. O maior valor é {}.'.format(media, menor, maior))'''