print('Desafio 031 - Custo da Viagem')

print("""Desenvolva um programa que pergunte a distância de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.""")

km = float(input('Digite a distância da viagem: '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('Para uma viagem de {} km, o valor da passagem será de R$ {:.2f}. Faça uma boa viagem!'.format(km, preço))

#preço = km * 0.50 if km <= 200 else km * 0.50 - IF SIMPLIFICADO

'''if km <= 200:
    print('Para uma viagem de {} km, o valor da passagem será R$ {:.2f}. Faça uma boa viagem!'.format(km, km*0.50))
else:
    print('Para uma viagem de {} km, o valor da passagem será R$ {:.2f}. Tenha uma boa viagem!'.format(km, km*0.45))''' MEU EXERCÍCIO
