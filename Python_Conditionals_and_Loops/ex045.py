from random import choice
from time import sleep

jogador=str(input('Qual é a sua jogada?')).strip().capitalize()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

jokenpo=['Pedra', 'Papel', 'Tesoura']

machina=choice(jokenpo)

print(f'{machina}!')
sleep(1)

if jogador == machina:
    print('Empatamos! Vamos de novo?')
elif jogador == 'Pedra' and machina == 'Papel':
    print('Eu ganhei! Papel enrola pedra hihihi')
elif jogador == 'Papel' and machina == 'Tesoura':
    print('Eu ganhei! Tesoura corta papel hahaha')
elif jogador == 'Tesoura' and machina == 'Pedra':
    print('Eu ganhei! Pedra quebra tesoura!')
elif jogador == 'Papel' and machina == 'Pedra':
    print('Você ganhou! Papel enrola pedra. Vamos de novo?')
elif jogador == 'Tesoura' and machina == 'Papel':
    print('Você ganhou! Tesoura corta papel. Mais uma vez?')
elif jogador == 'Pedra' and machina == 'Tesoura':
    print('Você ganhou! Pedra quebra tesoura. Acho que já brincamos o suficiente.')