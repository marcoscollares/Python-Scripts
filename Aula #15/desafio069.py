print('Desafio 69 - Análise de Dados do Grupo')
print('''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, \no programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. ''')
print('\033[1;31m=\033[m'*30)
print('      \033[1;34mREGISTRO DE GRUPOS\033[m')
print('\033[1;31m=\033[m'*30)
homem = mulher = pessoa = maior = 0
while True:
    idade = int(input('Quantos anos a pessoa tem? '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo da pessoa? [F/M] ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    pessoa += 1
    if sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade < 20:
        mulher += 1
    ask = ' '
    while ask not in 'SN':
        ask = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if ask in 'Nn':
        break
print(f'Um número de {pessoa} pessoas foram registradas no total. Dentre elas, {homem} são homens.')
print(f'{mulher} mulheres são menores de 20 anos. Porém, {maior} do total de pessoas têm mais de 18 anos')
