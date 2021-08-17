""" [DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta.
Analise seus comprimentos e diga se é possível formar um triângulo com essas
retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento
de cada lado deve ser menor que a soma dos outros dois.
"""
line1 = float(input('Set a line segment: '))
line2 = float(input('Set other line segment: '))
line3 = float(input('Set another line segment: '))

if line1 + line2 > line3 and line2+line3 > line1 and line1+line3> line2:
    print('You can form a triangle with these segments.')



