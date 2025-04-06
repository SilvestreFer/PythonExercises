import emoji

numero=int(input('Digite um número inteiro: '))
total=0

print(emoji.emojize(f'Vou mostrar por quais números {numero} é divisível em \033[32mVERDE\033[m :smiling_face:'))5

for c in range(1, numero+1):
    if numero % c == 0:
        print('\033[32m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}',end=' ')

print(f'\n\033[mO número {numero} foi divisível {total} vezes.')

if total == 2:
    print(emoji.emojize('E por isso ele é PRIMO!:T-Rex:'))
else:
    print('E por isso, ele \033[31mNÃO\033[m é PRIMO')
