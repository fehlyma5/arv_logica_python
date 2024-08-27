print('crie um programa que enha uma upla com varias palavras (nao usar acento).\n'
      'depois disso, voce deve mostrar, para cda palavra, quis sao suas vogais')

palavras  = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'estudar', 'praticar',
           'trabalhar', 'mercado', 'programador', 'future')
for p in palavras:
      print(f'\nNa palavra \033[1;34m {p.upper()}\033[m temos ', end='') #aqui foi dado o metodo UPPER p deixar as palavrasm caixa alta
      for letra in p:
            if letra.lower() in 'aeiou': #aqui foi usado LOWER para reconhecer as minusculas
                  print(letra, end=' ')
