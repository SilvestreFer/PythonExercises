from time import sleep

primeiro_número = int(input('Digite o 1º número: '))
segundo_número = int(input('Digite o 2º número: '))
sleep(1)

opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] saber qual o maior
    [4] digitar novos números
    [5] sair do programa''')
    opção = int(input('>>>>>>>>>> Qual a sua opção? '))
    if opção == 1:
        soma = primeiro_número + segundo_número
        print(f'A soma de {primeiro_número} e {segundo_número} é {soma}.')
    elif opção == 2:
        produto = primeiro_número * segundo_número
        print(f'O produto entre {primeiro_número} e {segundo_número} é {produto}.')
    elif opção == 3:
        if primeiro_número > segundo_número:
            print(f'{primeiro_número} é maior que {segundo_número}.')
        elif segundo_número > primeiro_número:
            print(f'{segundo_número} é maior que {primeiro_número}.')
        elif primeiro_número == segundo_número:
            print('Os valores são iguais!')
    elif opção == 4:
        print('Informe os números novamente: ')
        primeiro_número = int(input('Digite o 1º número: '))
        segundo_número = int(input('Digite o 2º número: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    print('_'*25)
print('Fim do programa! Volte sempre!')
