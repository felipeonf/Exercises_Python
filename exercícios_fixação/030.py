'''
[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes
'''
line1 = float(input('Set a line segment: '))
line2 = float(input('Set other line segment: '))
line3 = float(input('Set another line segment: '))

if line1 + line2 > line3 and line2+line3 > line1 and line1+line3> line2:
    print('You can form a triangle with these segments.')
    triangule = True
else:
    print('You cannot form a triangule with these segments.')
    print('The program will exit.')
    exit() 
       
if triangule == True:
    if line1 == line2 and line1 == line3 and line2== line3:
        print('That triangule is Equilater.')
    elif line1 == line2 and line3 != line1 and line2!=line3 or line3 == line2 and line3 != line1\
        and line2 != line1 or line1 == line3 and line1 != line2 and line2 != line3:
        print('That triangule is Iso.')

    elif line1 != line2 and line1 != line3\
        and line2!= line3:
        print('That triangule is Escalen.')





