resposta = 'S'
soma = 0
quantidade = 0
média = 0

while resposta in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quantidade += 1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = número
    resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]

média = soma / quantidade
print(f'Você digitou {quantidade} e a média foi {média}.')
print(f'O maior valor foi {maior} e o menor {menor}.')