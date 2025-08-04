total_compra = maior_mil = menor_preco = contador = 0
barato = ' '
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço do produto: R$'))
    contador += 1

    total_compra += preco

    if preco > 1000:
        maior_mil += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break

print(f'{" FIM DO PROGRAMA ":=^40}')
print(f'O total gasto na compra foi de R$ {total_compra:.2f}.')
print(f'Temos {maior_mil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {barato}.')
