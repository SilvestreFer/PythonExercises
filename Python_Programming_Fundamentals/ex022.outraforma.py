#Part 01:
nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')
print(f'Seu nome em letras maiúsculas é {nome.upper()}')

#Parte 02:
print(f'Seu nome em letras minúculas é {nome.lower()}')

#Parte 03: ********************
print(f'Seu nome ao todo tem {len(nome) - nome.count(' ')}.')

#Parte 04:
print(f'Seu primeiro nome tem {nome.find(' ')}.')