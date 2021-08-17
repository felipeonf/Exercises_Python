values = []
for value in range(5):
    values.append(int(input('Submit a number: ')))
print(values)
print(f'The max value in the list is {max(values)} and the min value is {min(values)}')
print(f'The max value appears in the',end=' ')
for position in range(5):
    if values[position] == max(values):
        print(f'{position+1}°',end=' ')
print('positions')
print(f'The min value appears in the',end=' ')
for position in range(5):
    if values[position] == min(values):
        print(f'{position+1}°',end=' ')
print('positions')
