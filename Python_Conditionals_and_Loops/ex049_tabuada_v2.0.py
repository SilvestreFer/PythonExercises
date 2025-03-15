from time import sleep

n=int(input('Digite um número para saber a sua tabuada: '))
print(f'A tabuada de {n} é: ')
sleep(1)

print('-='*11)
sleep(1)
for c in range (1,11):
    tabuada = n * c
    print(f'{n}x{c}={tabuada}')
    sleep(1)
print('-='*11)

print('Bons estudos!')
