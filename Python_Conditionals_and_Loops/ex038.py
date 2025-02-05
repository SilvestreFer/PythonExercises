primeiro=int(input('Digite um número: '))
segundo=int(input('Digite outro: '))

if primeiro > segundo:
    print(f'{primeiro} é maior que {segundo}!')

elif primeiro < segundo:
    print(f'{segundo} é maior que {primeiro}!')

elif primeiro == segundo:
    print(f'Os dois valores são iguais!')
    #I could use 'else' as well once there is no 4th option mathematically