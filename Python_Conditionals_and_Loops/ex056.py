pessoa = []
soma_de_idade = 0
homem_mais_velho = {"nome": "", "idade": 0}
mulheres_menos_20 = 0

for i in range(4):
    print(f'Sobre a pessoa {i+1}')
    nome=input('Nome: ')
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [F]/[M]: ')).strip().upper()

    soma_de_idade += idade

    if sexo == "M" and idade > homem_mais_velho["idade"]:
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade

    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

#Calculando a médio de idade do grupo:
media=soma_de_idade/4

#Apresentando os resultados:
print(f'A média de idade do grupo é {media:.0f} anos')

if homem_mais_velho["nome"]:
    print(f'O homem mais velho é {homem_mais_velho["nome"]} com {homem_mais_velho["idade"]} anos.')
else:
    print('Não há homens no grupo.')

if mulheres_menos_20 == 1:
    print(f'O grupo tem {mulheres_menos_20} mulher com menos de 20 anos de idade.')
elif mulheres_menos_20 == 0:
    print(f'Não há mulheres com menos de 20 anos no grupo.')
else:
    print(f'O grupo tem {mulheres_menos_20} mulheres com menos de 20 anos de idade.')
