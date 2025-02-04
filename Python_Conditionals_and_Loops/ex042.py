from time import sleep

print('Vou te contar se os segmentos de reta que você tem formam um triângulo.')

sleep(2)

segmento1 = float(input('Digite o valor do primeiro segmento em cm: '))
segmento2 = float(input('Digite o segundo segmento em cm: '))
segmento3 = float(input('Digite o terceiro segmento em cm: '))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:
    print(f'Os segmentos de reta {segmento1}cm, {segmento2}cm e {segmento3}cm formam um triângulo :)')
    sleep(1)
    print(f'O perímetro do seu triângulo vai ser {segmento1+segmento2+segmento3}cm.')
    sleep(1)
    if segmento1 == segmento2 and segmento1 == segmento3:
        print('O seu triângulo vai ser EQUILATERO.')
    elif segmento1 == segmento2 or segmento1 == segmento3 or segmento2 == segmento3:
        print('O seu triângulo vai ser ISÓSCELES.')
    else:
        print('O seu triângulo vai ser ESCALENO.')
else:
    print(f'Os segmentos de reta {segmento1}cm, {segmento2}cm e {segmento3}cm NÃO FORMAM um triângulo. Sinto muito!')
