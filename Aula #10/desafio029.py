print('Desafio 29 - Radar Eletrônico')

print("""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem 
dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.""")

vel = float(input('Digite a velocidade registrada: '))
if vel > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade de 80 Km/h!!!')
    print('Portanto, você deverá pagar o valor de R$ {:.2f}!'.format((vel-80)*7))
print('Tenha um bom dia. Dirija com segurança!')

#if vel > 80:
 #   print('Você foi multado e deverá pagar o valor de R$ {:.2f}!'.format((vel - 80) * 7))

#else:
  #  print('Tenha um bom dia. Dirija com segurança!')

