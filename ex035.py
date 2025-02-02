print('Vou te contar se os segmentos de reta que você tem formam um triângulo B)')

segmento1 = float(input('Digite o valor do primeiro segmento em cm: '))
segmento2 = float(input('Digite o segundo segmento em cm: '))
segmento3 = float(input('Digite o terceiro segmento em cm: '))

if segmento1 + segmento2 > segmento3 and segmento1 + segmento3 > segmento2 and segmento2 + segmento3 > segmento1:
    print(f'Os segmentos de reta {segmento1}cm, {segmento2}cm e {segmento3}cm formam um triângulo :)')
    print(f'O perimetro desse triângulo vai ser {segmento1+segmento2+segmento3}cm.')

else:
    print(f'Os segmentos de reta {segmento1}cm, {segmento2}cm e {segmento3}cm NÃO FORMAM um triângulo. Sinto muito!')