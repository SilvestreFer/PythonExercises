for c in range (1,6):
    print('Oi!')
    #mostra 5 vezes o 'oi', porque o python ignora o último número.
    #se eu quiser mostrar 6 vezes, escrevo (1,7)
print('-='*11)

for c in range (6,0,-1):
    print(c)
    #vai mostrar os números em ordem decrescente pelo '-1' no final da linha
print('-='*11)

for c in range (0,7,2):
    print(c)
    #vai mostrar os números pulando de 2 em 2 pelo '2' no final da linha
print('-='*11)

n = int(input('Digite um número: '))
for c in range (0,n):
    print(c)
print('-='*11)

n = int(input('Digite um número: '))
for c in range (0,n+1):
    print(c)
    #para ir até o número digitado
print('-='*11)
