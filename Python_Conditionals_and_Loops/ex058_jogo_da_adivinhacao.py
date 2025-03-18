from random import randint
import emoji

print('''Sou seu computador... Acabei de pensar em um número entre 0 e 10.
Você consegue adivinhar que número eu pensei? ''')

#Fazendo o computador "pensar" um número
número_computador = randint(0,10)

#Definindo as variáveis para o loop
número_usuário = 0
palpite = 0

while número_usuário != número_computador:
    número_usuário =int(input('Qual número eu estou pensando? '))
    if número_usuário == número_computador:
        print(emoji.emojize(f'Você respondeu {número_usuário}! Você acertou o número que eu pensei :grinning_face_with_big_eyes:'))
    else:
        print(f'Eu não pensei em {número_usuário}. Tente mais uma vez.')
    palpite += 1
if palpite == 1:
    print(emoji.emojize('Você só precisou de um palpite para acertar! Leu minha mente! :brain:'))
else:
    print(f'Você precisou de {palpite} palpites para acertar!')
print(emoji.emojize('Fim do jogo ! :fireworks:'))