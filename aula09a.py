frase='Curso em Vídeo Python'

#Fatiamento:

print(frase[9])
print(frase[9:13])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

#Análise

print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação

frase2='     Curso em Vídeo Python      '

print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())

#Divisão

print(frase.split())

#Junção

print('-'.join(frase))
print(' '.join(frase))
# Lembrar de colocar o ponto entre a união e o join

#Imprimir texto longo:

print("""
I hope you found this guide to mastering NLP helpful. Here’s a review of the 7 steps:

Step 1: Python and ML fundamentals 
Step 2: Deep learning fundamentals
Step 3: NLP 101 and essential linguistics concepts
Step 4: Traditional NLP techniques
Step 5: Deep learning for NLP
Step 6: NLP with transformers
Step 7: Build projects, keep learning, and stay current!
If you’re looking for tutorials, project walkthroughs, and more, check out the collection of NLP resources on KDnuggets.""")