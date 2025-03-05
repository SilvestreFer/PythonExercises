from time import sleep

soma_idade = 0
media_idade = 0
homem_mais_velho_idade = 0
homem_mais_velho = ''
total_mulheres = 0

for pessoa in range (1,5):
    print(f'------ {pessoa}ª PESSOA ------')
    nome=str(input('Nome da pessoa: ')).strip().upper()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    if pessoa == 1 and sexo in 'Mm':
        homem_mais_velho_idade = idade
        homem_mais_velho = nome
    if sexo in 'Mm' and idade > homem_mais_velho_idade:
        homem_mais_velho_idade = idade
        homem_mais_velho = nome
    if sexo in 'Fm' and idade < 20:
        total_mulheres += 1

print('Analisando os dados...')
sleep(1)

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade}.')
print(f'O homem mais velho tem {homem_mais_velho_idade} anos e se chama {homem_mais_velho}.')

if total_mulheres == 1:
    print(f'Ao todo temos 1 mulher com menos de 20 anos.')
else:
    print(f'Ao todo são {total_mulheres} mulheres com menos de 20 anos.')
