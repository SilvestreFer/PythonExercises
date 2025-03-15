from time import sleep

soma_de_idade = 0
homem_mais_velho = {"nome": "", "idade": 0, "sexo":"M"}
mulheres_menos_20 = []

for i in range(4):
    #Coletando dados:
    print(f'Sobre a pessoa {i+1}')
    nome=str(input('Nome: ')).strip().title()
    idade=int(input('Idade: '))
    sexo=str(input('Sexo [F]/[M]: ')).strip().upper()

    #Equação para o calculo da média:
    soma_de_idade += idade

    #Condição para encontrar o homem mais velho:
    if sexo == "M" and idade > homem_mais_velho["idade"]:
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade

    #Condição para contar as mulheres com menos de 20 anos:
    if sexo == "F" and idade < 20:
        mulheres_menos_20.append(nome)

#Calculando a médio de idade do grupo:
media=soma_de_idade/4

#Apresentando os resultados:

print('Analisando o grupo.', end="")
sleep(1)
print('.', end="")
sleep(1)
print('.')

#Média:
print(f'A média de idade do grupo é {media:.0f} anos.')
sleep(1)

#Homem mais velho:
if homem_mais_velho["nome"]:
    print(f'O homem mais velho é {homem_mais_velho["nome"]} com {homem_mais_velho["idade"]} anos.')
else:
    print('Não há homens no grupo.')
sleep(1)

#Mulheres:
if len(mulheres_menos_20) == 1:
    print(f'O grupo tem 1 mulher com menos de 20 anos: {", ".join(mulheres_menos_20)}.')
elif len(mulheres_menos_20) == 0:
    print(f'Não há mulheres com menos de 20 anos no grupo.')
else:
    print(f'O grupo tem {len(mulheres_menos_20)} mulheres com menos de 20 anos: {", ".join(mulheres_menos_20)}.')
