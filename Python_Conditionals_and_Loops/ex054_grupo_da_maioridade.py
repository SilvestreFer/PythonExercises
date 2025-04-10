from datetime import date
from time import sleep

soma_maiores=0
soma_menores=0

print('Vamos ver quantas pessoas já atingiram a maioridade no seu grupo de 7? ')
sleep(1)

for c in range(7):
    birth=int(input(f'Digite o ano de nascimento da pessoa {c + 1}: '))
    if date.today().year - birth >= 21:
        soma_maiores+=1
    elif date.today().year - birth < 21:
        soma_menores+=1

if soma_maiores == 1:
    print(f'Há uma pessoa maior de idade.')
else:
    print(f'{soma_maiores} pessoas atingiram a maioridade!')
if soma_menores == 1:
    print(f'Há uma pessoa menor de idade.')
else:
    print(f'{soma_menores} pessoas ainda NÃO atingiram a maior idade!')
