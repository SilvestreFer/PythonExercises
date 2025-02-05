numero=int(input('Digite o número que deseja converter: '))
base=str(input('Para qual base deseja converter? ')).strip().lower()

if base in ['binária', 'binaria', 'binário', 'binario']:
    print(f'A versão binária de {numero} é', bin(numero))

elif base in ['octal','oct', 'oc']:
    print(f'A versão octal de {numero} é', oct(numero))

elif base in ['hexadecimal', 'hexa', 'hex']:
    print(f'A versão hexadecimal de {numero} é?', hex(numero))