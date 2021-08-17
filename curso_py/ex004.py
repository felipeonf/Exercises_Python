frase = str(input('Digite um frase: ')).lower().strip()


print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira aparição da letra A na frase é a posição {}'.format(frase.find('a')+1))
print('A ultima aparição da letra A na frase é a posição {}'.format(frase.rfind('a')+1))



    
