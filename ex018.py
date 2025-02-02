import math

#O Python não calcula os ângulos em celcius, mas sim em redianos.
ângulo=float(input('Digite o valor do ângulo: '))

#Então converto radianos:
#ar, significa ângulos radianos
ar=math.radians(ângulo)

#Agora calculo os sin, cos e tan:
seno=math.sin(ar)
cosseno=math.cos(ar)
tangente=math.tan(ar)

print(f'O seno de {ângulo} é {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}.')