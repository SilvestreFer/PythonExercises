num=float(input('Digite um número real: '))
partint=int(num)
print(f'A parte inteira do número real {num} é {partint}.')

import math
partarr=round(num)
print(f'Se a arredondar o número real {num}, ele será {partarr}')
print(f'O número arredondado para mais é {math.ceil(num)}')
print(f'O número arredondado para menos é {math.floor(num)}')