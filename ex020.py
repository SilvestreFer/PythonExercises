import random

aluno1=input('Primeiro aluno: ')
aluno2=input('Segundo aluno: ')
aluno3=input('Terceiro aluno: ')
aluno4=input('Quarto aluno: ')

alunos=[aluno1,aluno2,aluno3,aluno4]

apresentação=random.sample(alunos, 4)

print("A ordem da apresentação do trabalho será:")
for i, aluno in enumerate(apresentação, start=1):
    print(f''
          f'{i}. {aluno}')
