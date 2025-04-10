print('Hora de somar números!')
print('Digite 999, se não quiser mais adicionar números.')

numero = 0
contador = 0
soma = 0
#Como as três variáveis começam com 0, eu poderia escrever numero = contador = soma = 0

while numero != 999:
    contador += 1
    soma += numero
    numero = int(input('Digite um número para a soma: '))
print(f'Você digitou {contador-1} números e a soma entre eles é {soma}.')
