print('-'*20)
print('GERADOR DE TABUADA')
print('-'*20)

numero = 1
while numero > -1:
    numero = int(input('Digite um número para saber sua tabuada: '))
    if numero < 0:
        print('PROGRAMA ENCERRADO')
        break
    for c in range (1,11):
        print(f'{numero}x{c} = {numero*c}')