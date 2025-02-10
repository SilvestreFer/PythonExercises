from time import sleep
import emoji

#Primeiro testei se o número pode divir por 3:

n = int(input('Digite um número: '))
print('Analisando o número .', end=" ")
sleep(1)
print('.', end=" ")
sleep(1)
print('.')

if n %3 == 0:
    print(f'{n} é divisível por 3 {emoji.emojize(":sign_of_the_horns:")}.')
else:
    print(f'{n} não é divisível por 3.')

#Depois testei se é impar:

if n %2 == 1:
    print(f'{n} é impar!')
else:
    print(f'{n} é par!')

#Juntei as duas condições:

if n %3 == 0 and n %2 == 1:
    print(f'{n} é multiplo de três e é impar.')
elif n %3 == 0 and n%3 == 0:
    print(f'{n} é divisível por 3, mas não é impar.')
print('-='*11)

#Colocando na estrutura de repetição para calcular a soma dos impares múltiplos de 3 no intervalo de 1 a 500:
print(emoji.emojize('Agora vou somar todos os números impares múltiplos de 3 até 500 :smiling_face:'))
sleep(2)
s = 0
for c in range(1,500):
    if c%3==0 and c%2==1:
        s += c
print(f'A soma dos números impares múltiplos de 3 entre 1 e 500 é \033[035m{s}\033[m.')
#O print fica fora do for, porque só quero apresentar o total final e não a soma número por número no loop
print('Fim do exercício!')