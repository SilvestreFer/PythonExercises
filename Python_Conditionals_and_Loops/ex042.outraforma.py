segm1 = float (input('Primeiro segmento: '))
segm2 = float (input('Segundo segmento: '))
segm3 = float (input('Terceiro segmento: '))

if segm1 < segm2 + segm3 and segm2 < segm1 + segm3 and segm3 < segm1 + segm2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    #o end='' no final é para não concluir a frase em "triângulo e seguir com a linha da próxima condição
    if segm1 == segm3 == segm2:
        print('EQUILÁTERO!')
    elif segm1 != segm2 != segm3 != segm1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO podem formar um triângulo!')