import random
from time import sleep as sl
numero_aleatorio = random.choice([0, 1, 2, 3, 4,5])
print('Eu estou pensando em um número entre 0 e 5...')
numero_chute = int(input('Qual número eu estou pensando? '))
print('Processando...')
sl(3)
if numero_chute == numero_aleatorio:
    print('Parabéns! Você leu minha mente! Você venceu!')
else:
    print(f'Na verdade, eu pensei no número {numero_aleatorio}. Você perdeu!')