print('-='*5,'GERADOR DE PA','=-'*5)

primeiro_termo = int(input('Qual o primeiro termo da PA? '))
razão = int(input('Qual a razão da PA? '))

termos = primeiro_termo
contador = 0

print(f'Estes são os 10 primeiros termos da PA:')
while contador < 10:
    print(termos, end=' ➔ ')
    termos += razão
    contador += 1
print(f'FIM')
