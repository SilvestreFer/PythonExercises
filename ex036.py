casa=float(input('Qual o valor da casa? R$'))
salario=float(input('Qual é o seu salário atual? R$'))
anos=int(input('Em quantos anos pretende quitar a casa? R$'))

parcelas=anos*12
prestacao=casa/parcelas

if prestacao > salario*0.3:
    print('Infelizmente não podemos conceder esse emprestimo.')
else:
    print(f'O seu emprestimo fica em {parcelas:.0f} vezes de R${prestacao:.2f}. Deseja seguir com o emprestimo?')