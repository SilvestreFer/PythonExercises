from random import choice
from time import sleep

jokenpo=['Pedra', 'Papel', 'Tesoura']

jogador=str(input('Jo - Ken - Pô ?')).strip().capitalize()
machina=choice(jokenpo)

print(f'Eu escolhi {machina}.')

sleep(1)

if jogador == machina:
    print('Empatamos! Vamos de novo?')
elif jogador == 'pedra' and machina == 'Papel':
    print('Eu ganhei! Papel enrola pedra hihihi')
elif jogador == 'papel' and machina == 'Tesoura':
    print('Eu ganhei! Tesoura corta papel hahaha')
elif jogador == 'tesoura' and machina == 'Pedra':
    print('Eu ganhei! Pedra quebra tesoura! Beijos!')
elif jogador == 'papel' and machina == 'Pedra':
    print('Você ganhou! Papel enrola pedra. Vamos de novo?')
elif jogador == 'tesoura' and machina == 'Papel':
    print('Você ganhou! Tesoura corta papel. Mais uma vez?')
elif jogador == 'pedra' and machina == 'Tesoura':
    print('Você ganhou! Pedra quebra tesoura. Acho que já brincamos o suficiente. Tchau!')