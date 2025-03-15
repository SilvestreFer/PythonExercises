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


termos = primeiro_termo
contador = 0
total = 0
mais_termos = 10

while mais_termos != 0:
    total += mais_termos
    while contador < total:
        print(termos, end= ' ➔ ')
        termos += razao
        contador += 1
    print('PAUSA')
    mais_termos = int(input('Deseja ver mais quantos termos?'))
print(f'Progressão finalizada com {total} termos mostrados!')