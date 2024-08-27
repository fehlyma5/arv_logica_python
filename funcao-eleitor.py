print("Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro \n"
      "o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.")
print("=*"*100)

def voto(ano):
    from datetime import date #aqui to importando a biblioteca dentro da função p economizar espaço na memoria
    atual = date.today().year
    idade = atual - ano
    if idade >=16 and idade <= 18 or idade > 65:
        return f"a pessoa com {idade} possui voto no caso OPCIONAL"
    elif idade < 16:
        return f"a pessoa com {idade} possui Voto Negado, ainda não habilitada para votar"
    else:
        return f"a pessoa com {idade} possui voto OBRIGATORIO"

nasc = int(input("Informe ano do seu nascimento: (ex: 1111) "))
print(voto(nasc))
#na nossa funçao pela primeira vez usamos return ao inves do print nas condicionais
#o return nao precisa a declarado dentro de parenteses iguais o print
#quando se vai chamar a função declarada nao precisa dos dois pontos no final