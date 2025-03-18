sexo = str(input('Digite o seu sexo: [M/F]')).strip().upper()[0]

while sexo not in ['M', 'F']:
    sexo = str(input('Dados inválido. Por favor, digite o seu sexo: [M/F]')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
