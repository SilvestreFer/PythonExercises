print('-='*11,'GERADOR DE PA','=-'*11)

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

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
