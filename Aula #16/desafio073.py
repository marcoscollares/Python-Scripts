print('Desafio 73 - Tuplas com Times de Futebol')
print('''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.''')

print('\033[1;33m=-\033[m'*20)
print(f'\033[1m{"TABELA DO BRASILEIRÃO 2020":^40}\033[m')
print('\033[1;33m-=\033[m'*20)

vinte = ('Corínthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo', 'Athlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('\033[1;32m~\033[m'*20)
print(f'Lista de times do Brasileirão 2020: \033[1;36m{vinte}\033[m')
print('\033[1;32m~\033[m'*20)
print(f'Os 5 primeiros colocados: \033[1;36m{vinte[:5]}\033[m')
print('\033[1;32m~\033[m'*20)
print(f'Os últimos 4 colocados: \033[1;36m{vinte[-4:]}\033[m')
print('\033[1;32m~\033[m'*20)
print(f'Times em ordem alfabética: \033[1;36m{sorted(vinte)}\033[m')
print('\033[1;32m~\033[m'*20)
print(f'O Chapecoense está na \033[1;36m{vinte.index("Chapecoense")+1}ª\033[m posição')
print('\033[1;32m~\033[m'*20)
