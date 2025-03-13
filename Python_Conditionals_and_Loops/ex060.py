número = int(input('Digite um número para calcular o fatorial: '))

#Calculando com 'while'
fatorial = 1
while número > 1:
    fatorial *= número
    número -=1
print(f'O fatorial de {número} é: {fatorial}')

#Calculando com 'for'
for contador in range (1, número+1):
    fatorial *= contador
print(f'O fatorial de {número} é: {fatorial}')