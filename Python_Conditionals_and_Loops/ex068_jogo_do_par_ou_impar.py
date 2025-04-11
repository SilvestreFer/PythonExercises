from random import randint

print('-=-'*20)
print('Vamos jogar PAR ou ÍMPAR!')
print('-=-'*20)

vitoria = 0 #começando a variável fora para acumular no while.

while True:
    #recebendo sempre valores novos a cada partida
    pessoa = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = pessoa + computador
    tipo = ''
    while tipo not in ['P','I']:
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]

    #analisando a partida
    print(f'Você jogou {pessoa} e o computador {computador}. O total é {soma}.')
    print('Deu PAR! ' if soma %2 == 0 else 'Deu ÍMPAR! ', end='')

    if tipo == 'P':
        if soma%2 == 0:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if soma%2 == 1:
            print('Você venceu!')
            vitoria += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {vitoria} vezes.')
