# triangulos e seus tipos
line1 = float(input('Set a line segment: '))
line2 = float(input('Set other line segment: '))
line3 = float(input('Set another line segment: '))
if line1 + line2 > line3 and line2+line3 > line1 and line1+line3> line2:
    print('You can form a triangle ',end= '')
    if line1 == line2 == line3:
        print('EQUILATER!')
    elif line1 != line2 != line3 != line1:
        print('ESCALEN!')
    else:
        print('ISO!')
else:
    print('You cannot form a triangule with these segments.')
    print('The program will exit.')
    exit() 

       
