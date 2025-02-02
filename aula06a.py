n0=input('Digite um valor:')
print(type(n0))

n1=int(input('Digite um valor:'))
n2=int(input('Digite outro:'))
s=n1+n2
# print('A soma entre{} '.format(n1),'e {} é'.format(n2),s,'.')
#print('A soma entre {} e {} vale {}.'.format(n1, n2, s))
# Ex.: ('A soma entre {1} e {2} vale {3}.'.format(n1, n2, s))
print(f'A soma entre {n1} e {n2} vale {s}')

