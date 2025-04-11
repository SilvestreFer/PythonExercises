numero = 0
digitados = 0
soma = 0

while numero != 999:
    numero = int(input('Digite um número (ou 999 para parar):'))
    if numero == 999:
        break
    digitados += 1
    soma += numero

print(f'Você digitou {digitados} números e a soma entre eles é {soma}.')
