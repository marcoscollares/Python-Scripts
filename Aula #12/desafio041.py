import datetime
print('\033[1;4mDesafio 41 - Classificando Atletas\033[m')
print('\033[1;35m»\033[m'*70)
print('                         \033[1;4mCADASTRO DE ATLETAS\033[m')
print('\033[1;35m«\033[m'*70)
print("""\033[1mA Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER\033[m""")

ano = int(input('Digite o ano de nascimento do atleta: '))
sistema = datetime.date.today().year
calculo = ano - sistema
if calculo <= 9:
    print('O atleta faz parte da CATEGORIA MIRIM.')
elif calculo > 9 and calculo<= 14:
    print('O atleta faz parte da CATEGORIA INFANTIL.')
elif calculo > 14 and calculo <= 19:
    print('O atleta faz parte da CATEGORIA JÚNIOR.')
elif calculo > 19 and calculo <=25:
    print('O atleta faz parte da CATEGORIA SÊNIOR.')
elif calculo > 25:
    print('O atleta faz parte da CATEGORIA MASTER.')
