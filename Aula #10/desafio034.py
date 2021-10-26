print('Desafio 34 - Aumentos múltiplos')

print("""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.""")

sal = float(input('Digite o valor do salário do funcionário: '))

if sal > 1250:
    novo = (sal*10)/100+sal
else:
    novo = (sal*15)/100+sal
print('O salário reajustado será de R$ {:.2f}.'.format(novo))