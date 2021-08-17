cidade = input('Digite o nome da sua cidade: ')
sep = cidade.strip().upper().split()
if sep[0] == 'SANTO':
    print('Sua cidade foi inspirada em um santo.')
else:
    print('Sua cidade não foi inspirada em um santo.')


