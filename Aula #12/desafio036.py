print('\033[1;4mDesafio 36 - Aprovando Empréstimo\033[m')

print('\033[1mEscreva um programa para aprovar o empréstimo bancário para a compra de uma casa. \nPergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. \nA prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.\033[m')

valor = float(input('Digite o valor da casa a ser financiada: '))
salario = float(input('Digite o valor do salário do cliente: '))
anos = int(input('Digite a quantidade de anos: '))
mensalidade = anos * 12
prestacao = valor / mensalidade
porcentagem = (salario * 30) / 100

if prestacao <= porcentagem:
    print('\033[36mParabéns! O teu empréstimo foi aprovado! O valor da prestação será de R$ {:.2f} e você deverá pagar em {} anos.\033[m'.format(prestacao, anos))
else:
    print('\033[31mLamento. Infelizmente você nao pode financiar esta casa!\033[m')

