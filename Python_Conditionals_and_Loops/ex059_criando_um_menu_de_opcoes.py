primeiro_número = int(input('Digite o 1º número: '))
segundo_número = int(input('Digite o 2º número: '))

print('O que desejas fazer com esses números?')
opção=int(input('''[1] somar
[2] multiplicar
[3] saber qual o maior
[4] digitar novos números
[5] sair do programa
'''))

if opção > 5:
    print('A opção não é valida! Reinicie o programa.')
else:
    while not opção == 5:
        if opção == 1:
            print(f'{primeiro_número}+{segundo_número}={primeiro_número+segundo_número}')
        elif opção == 2:
            print(f'{primeiro_número}x{segundo_número}={primeiro_número*segundo_número}')
        elif opção == 3:
            if primeiro_número > segundo_número:
                print(f'{primeiro_número} é o maior!')
            elif segundo_número > primeiro_número:
                print(f'{segundo_número} é o maior.')
            elif primeiro_número == segundo_número:
                print('Os valores são iguais!')
        elif opção == 4:
                primeiro_número = int(input('Digite o 1º número: '))
                segundo_número = int(input('Digite o 2º número: '))
        opção = int(input('''[1] somar
        [2] multiplicar
        [3] saber qual o maior
        [4] digitar novos números
        [5] sair do programa
        '''))
        print('Programa encerrado!')
