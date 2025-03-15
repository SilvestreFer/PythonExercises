print(f'{'LOJAS GUANABARA':-^40}')
produto=float(input('Qual é o preço do produto?'))
pagamento=str(input('Qual é a forma de pagamento: dinheiro ou cartão?')).strip().lower()

if pagamento in ['dinheiro','a vista', 'à vista']:
    desconto= produto - (produto*10/100)
    print(f'Com o pagamento à vista em dinheiro, você recebe 10% de desconto. '
          f'O valor do produto fica R${desconto:.2f}.')

elif pagamento in ['cartão', 'cartao']:
    parcelas=int(input('Qual o número de parcela para fazer o pagamento?'))
    if parcelas == 1:
        desconto= produto - (produto*5/100)
        print(f'Com o pagamento à vista no cartão, você recebe 5% de desconto.'
              f'O valor do produto fica R${desconto:.2f}.')

    elif parcelas == 2:
        mensalidade=produto/parcelas
        print(f'Com o parcelamento em 2x, não há acrescimo de juros. O valor do produto fica R${produto:.2f} em duas parcelas de R${mensalidade:.2f}.')

    elif 3 <= parcelas:
        juros= produto + (produto*20/100)
        mensalidade=juros/parcelas

        print(f'Com o parcelamento maior que 2x, é acrescentado juros de 20% ao valor do produto. '
              f'O valor do produto será R${juros:.2f} e cada parcela terá o valor R${mensalidade:.2f} mensais.')