from math import sqrt

co=float(input('Digite o valor do cateto oposto do seu triângulo retâgulo: '))
ca=float(input('Digite o valor do cateto adjacente do seu triângulo retâgulo: '))
hipotenusa=sqrt(co**2+ca**2)

print(f'O valor da hipotenusa do seu triângulo retângulo é {hipotenusa:.2f}')