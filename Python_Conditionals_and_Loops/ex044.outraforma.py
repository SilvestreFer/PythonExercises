print(f'{'LOJAS GUANABARA':-^40}')
preço=float(input('Qual é o preço das compras? R$'))
print('''FORMAS DE PAGAMENTO:
[1] à vista em dinheiro
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10/100)
elif opção == 2:
    total = preço - (preço * 5/100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x vezes de R${parcela:.2f} sem juros.')
elif opção == 4:
    total = preço + (preço * 20/100)
    nparcela = int(input('Quantas parcelas? '))
    parcela = total / nparcela
    print(f'Sua compra será parcelada em {nparcela} de R${parcela:.2f} COM JUROS.')
else:
    total = preço
    print('A opção de pagamento é \033[41minválida\033[m! Por favor, verifique a sua escolha.')
print(f'sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')