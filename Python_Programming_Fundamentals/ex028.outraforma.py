from random import randint
from time import sleep

#Fazendo o computador "pensar"
computador = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

#Jogador tenta adivinhar
jogador = int(input('Em que número pensei?'))
print('Processando...')
sleep(2)

#Mostrando o ganhador
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}.')
