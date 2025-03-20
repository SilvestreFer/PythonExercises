#Calculando fatorial com 'while'

número = int(input('Digite um número para calcular o fatorial: '))
contador =número
fatorial = 1
print(f'Calculando o {número}! =', end= ' ')
while contador > 0:
    print(f'{contador}', end=' ')
    print(f'x' if contador > 1 else '=', end=' ')
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
