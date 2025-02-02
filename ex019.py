from random import choice
#Poderia importar o random inteiro, mas nao uso as outras funções, então importei apenas o choice.

aluno1=input('Primeiro aluno: ')
aluno2=input('Segundo aluno: ')
aluno3=input('Terceiro aluno: ')
aluno4=input('Quarto aluno: ')

alunos=[aluno1,aluno2,aluno3,aluno4]
#Para o Python os [] criam uma lista.

print('O aluno sorteado para apagar o quadro é ',choice(alunos))
