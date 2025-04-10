numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break #paro o loop antes da soma
    soma += numero
print(f'A soma dos números é {soma}.')
print(f'Acabou')
