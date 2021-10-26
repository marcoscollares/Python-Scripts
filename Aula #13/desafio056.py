print('\033[1;4mDesafio 56 - Analisador Completo\033[m')
print('\033[1mDesenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade \ndo grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.\033[m')

maior = 0
menor = 0
totidade = 0
nomevelho = ''
homemvelho = 0
mulher = 0
for d in range(1,5):
    print('========== {}ª Pessoa =========='.format(d))
    nome = str(input('Digite o nome: ')).lstrip().capitalize()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).lstrip().upper()
    totidade += idade
    if d == 1 and sexo in 'M':
        nomevelho = nome
        homemvelho = idade
    if sexo in 'M' and idade > homemvelho:
        homemvelho = idade
        nomevelho = nome
    if sexo == 'F':
        if idade < 20:
            mulher += 1

media = totidade / 4
print('A média das idades do grupo é \033[1;33m{}\033[m anos.'.format(media))
print('A homem mais velho tem \033[1;31m{}\033[m anos e se chama \033[1;31m{}\033[m.'.format(homemvelho, nomevelho))
print('O número de mulheres menores de 20 anos no grupo é \033[1;35m{}\033[m.'.format(mulher))