#Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.

year = int(input('Give me a year: '))

if year % 4 == 0:
    if  year % 100 == 0 :
        print('That´s a common year.')
    else:
       print('That´s a leap year!')
elif year % 400 == 0:
    print('That´s a leap year!')

else:
    print('That´s a common year.')