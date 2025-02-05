from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL','TESOURA')
computador = randint(0,2)

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é sua jogada?'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*11)
print(f'Computador jogou \033[32m{itens[computador]}\033[m')
print(f'Jogador jogou \033[32m{itens[jogador]}\033[m')
print('-='*11)

if computador == 0: #computador jogou PEDRA
    if jogador == 0:
        print('EMPATE! Vamos de novo?')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE! Vamos de novo?')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE! Vamos de novo?')
    else:
        print('\033[31mJOGADA INVÁLIDA\033[m')