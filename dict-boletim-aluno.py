print('Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,\n'
      ' mostre o conteúdo da estrutura na tela.')
aluno = dict()
aluno['nome'] = str(input('NOME: '))
aluno['media'] = float(input(f'Media do {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO'
print('-=' * 30)
for k, v in aluno.items():
    print(f' - {k} = {v}')

