print('Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. \n'
      'Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.')

cont = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twoelven', 'thirty', 'fourten', 'fiveten', 'sixten', 'seventen', 'eighten', 'nineten', 'twenty')
while True:
    num = int(input('Enter a number 0 a 20: '))
    if 0<= num <= 20:
        print(f'You typed the option {cont[num]}')
#        print('Do you wish to continue? S -(yes) or N -(not)')
        resp = 's', 'n'
        if resp == 'S':
            num = int(input('Enter a number 0 a 20: '))
        else:
            print('Press 999 to exit.')
    else:
        print('Invalid Option, please enter a valid number.', end=' ')
    while num == 999:
        break
    if num == 999:
        break


