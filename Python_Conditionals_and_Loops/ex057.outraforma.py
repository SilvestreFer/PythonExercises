sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválido. Digite o seu sexo: [M/F] ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')