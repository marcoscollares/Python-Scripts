print('\033[1;4mDesafio - Gerenciador de Pagamentos\033[m')
print("""\033[1mElabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço formal
- Em 3x ou mais no cartão: 20% de juros\033[m""")

valor = float(input('Digite o valor do produto: '))
money = valor - (valor * 10)/100
cartao = valor - (valor * 5)/100
juros = valor + (valor * 20)/100
pag = int(input("""Para pagamento à vista com dinheiro ou cheque, digite 1.
Para pagamento à vista no cartão, digite 2.
Para pagamento parcelado 2x no cartão, digite 3.
Para pagamento parcelado 3x ou mais no cartão, digite 4.
Digite a forma de pagamento desejada: """))

if pag == 1:
    print('O valor do produto é \033[35;1mR$ {:.2f}\033[m, mas, pagando \033[33;1mà vista no dinheiro ou cheque\033[m, o preço total será \033[36;1mR$ {:.2f}\033[m.'.format(valor,money))

elif pag == 2:
    print('O valor do produto é \033[35;1mR$ {:.2f}\033[m, mas, pagando \033[33;1mà vista no cartão\033[m, o preço total será \033[36;1mR$ {:.2f}\033[m.'.format(valor, cartao))
elif pag == 4:
    numparc = int(input('Quantas parcelas: '))
    parcelas = valor / numparc
    juros = valor + (valor * 20 )/100
    print('O valor do produto é \033[35;1mR$ {:.2f}\033[m, mas, pagando \033[33;1mparcelado no cartão\033[m, o preço total será \033[36;1mR$ {:.2f}\033[m com juros. Com parcelas de \033[31;1m{} vezes de R$ {:.2f}\033[m.'.format(valor, juros, numparc, parcelas))
elif pag == 3:
    print('O valor do produto é \033[35;1mR$ {:.2f}\033[m'.format(valor))
elif pag > 4:
    print('Digite uma opção válida!')



