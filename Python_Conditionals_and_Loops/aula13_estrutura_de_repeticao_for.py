print('1- Conhecendo a estrutura:')

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

print('2- Explorando a estrutura:')

n = int(input('Digite um número: '))
for c in range (0,n):
    print(c)
print('-='*11)

n = int(input('Digite um número: '))
for c in range (0,n+1):
    print(c)
    #para ir até o número digitado
print('-='*11)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i,f+1,p):
    print(c)
print('-='*11)

for c in range(0,3):
    n = int(input('Digite um valor:'))
    #O comando dentro do for lê o comando quantas vezes estiver no range.
print('-='*11)

s = 0
for c in range(0,4):
    n = int(input('Digite um valor:'))
    s += n #o mesmo que "s=s+n" para o python
    # somando os input
print(f'O somatório de todos os valores foi {s}')