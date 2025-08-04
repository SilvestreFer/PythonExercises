maior_18 = homens = mulheres_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper() [0]
    if idade >= 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres_20 += 1

    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('Acabou')
print(f'Total de maiores de 18: {maior_18}')
print(f'Total de homens: {homens}')
print(f'Total de mulheres com menos de 20: {mulheres_20}')
