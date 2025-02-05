from datetime import date

atual=date.today().year
birth=int(input('Ano de nascimento: '))
idade=atual-birth

print(f'Quem nasceu em {birth} tem {idade} anos em {atual}.')

if idade == 18:
    print(f'Você tem que se alistar este ano!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
    ano = atual + saldo
    print(f'O seu alistamento será em {ano}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
    ano = atual - saldo
    print(f'Você já deveria ter se alistado em {ano}.')