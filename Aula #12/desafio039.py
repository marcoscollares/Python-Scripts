print('Desafio 39 - Alistamento Militar')
print("""Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou 
do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.""")

print('\033[1;35m=-=\033[m'*30)
print('\033[1m                            CONSULTORIA DE ALISTAMENTO MILITAR\033[m')
print('\033[1;35m=-=\033[m'*30)
import sys
from datetime import date
nome = input('Digite o teu nome: ')
sexo = str(input('Qual o teu sexo? (M/F): '))
if sexo == 'F':
    print('Olá, sra. {}. O alistamento militar não é obrigatório para você.'.format(nome))
    sys.exit()
alistou = input('Você já se alistou anteriormente? (S/N): ')
if alistou == 'S':
    print('Sr. {}, tudo está OK. Até mais!'.format(nome))
    sys.exit()
ano = int(input('Digite o ano do teu nascimento: '))
sistema = date.today().year
idade = sistema - ano

if idade > 18:
    print('\033[31mSr. {}, você está atrasado! Deveria ter se alistado há {} ano(s) atrás em {}. \nCompareça à Junta Militar mais próxima para fazer o teu alistamento!\033[m'.format(nome, idade - 18, sistema - (idade - 18)))

elif idade == 18:
    print('\033[36mSr. {}, está na hora do alistamento militar. Compareça à Junta Militar mais próxima para iniciar o teu processo.\033[m'.format(nome))
else:
    print('\033[33mSr. {}, obrigado por consultar, mas você ainda não tem idade para o alistamento militar. \nFaltam {} ano(s) para a tua vez chegar. Teu alistamento será em {}. \nEsperamos vê-lo mais tarde!\033[m'''.format(nome, 18 - idade, sistema + (18 - idade)))