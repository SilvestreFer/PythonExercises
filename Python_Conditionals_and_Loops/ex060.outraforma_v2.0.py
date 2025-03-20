#Calculando fatorial com 'for'

número = int(input('Digite um número para calcular o fatorial: '))
fatorial = 1

for contador in range (1, número+1):
    fatorial *= contador
print(f'O fatorial de {número} é: {fatorial}')
