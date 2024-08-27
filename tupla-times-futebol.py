print('Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, \n'
      'na ordem de colocação. Depois mostre:'
'''a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense''')

def detalhezin():
    print('='*100)


detalhezin()
times = ('palmeiras', 'fluminense', 'corinthians', 'flamengo', 'internacional', 'atletico-pr'
         'aletico-mg', 'santos', 'america-mg', 'bahia', 'bragantino', 'goias', 'sao paulo'
         'fortaleza', 'botafogo', 'ceara', 'cuiaba', 'avai', 'coritiba', 'atltico-go', 'juventude')
print(f'lista de times do brasileirao 2022 \033[1;33m {times} \033[m')
detalhezin()
print(f'Os 5 PRIMEIROS times são: \033[1;34m {times[:5]} \033[m')
detalhezin()
print(f'Os ultimos 4 times são: \033[1;35m {times [-4: ]} \033[m')
detalhezin()
print(f'Times em ordem alfabetica: \033[1;36m {sorted(times)} \033[m')
detalhezin()
print(f"A Botafogo encontra-se na \033[3;37m {times.index('botafogo')}º posição \033[m")
