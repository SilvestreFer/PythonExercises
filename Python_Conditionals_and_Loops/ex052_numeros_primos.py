import emoji
from time import sleep
n=int(input('Digite um número: '))

if n==1:
    print(emoji.emojize(f'{n} NÃO é um número primo!:T-Rex:'))
    print('Explicando.', end=" ")
    sleep(1)
    print('.', end=" ")
    sleep(1)
    print('.')
    print('Ele é um caso especial, porque não se encaixa na definição já que não tem dois divisores distintos.')

else:
    for c in range(2,n):
        if n%c==0:
            print(emoji.emojize(f'{n} NÃO é um número primo.:smiling_face_with_sunglasses:'))
            break #Sai do loop for imediatamente se encontrar um divisor. Não é preciso continuar testando se já achou um divisor.
    else:
        print(emoji.emojize(f'{n} é um número primo.:smiling_face:'))
