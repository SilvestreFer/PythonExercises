salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250.00:
    print(f'Com o aumento de 15%, esse funcionário deverá receber R${salario + (salario * 0.15):.2f}')
else:
    print(f'Com o aumento de 10%, esse funcionário deverá receber R${salario + (salario * 0.10):.2f}.')

#Outra forma de calcular: criando variaveis!
#novo = salario + (salario * 15 /100)
#novo = salario + (salario * 10/100)