print('-'*20)
print('GERADOR DE TABUADA')
print('-'*20)

while True:
    numero = int(input('Digite um número para saber sua tabuada: '))
    if numero < 0:
        print('-' * 20)
        print('PROGRAMA ENCERRADO')
        break
    print('-' * 20)
    for c in range (1,11):
        print(f'{numero}x{c} = {numero*c}')
    print('-' * 20)
