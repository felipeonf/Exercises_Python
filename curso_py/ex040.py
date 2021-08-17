#categoria atleta
from datetime import date
atual = date.today().year
ano = int(input('Digite seu ano de nascimento: '))
idade = atual - ano
if idade <= 9 :
    print('Sua categoria é MIRIM')
elif idade <= 14:
    print('Sua categoria é INFANTIL')
elif idade <= 19:
    print('Sua categoria é JUNIOR')
elif idade <= 25:
    print('Sua categoria é SENIOR')
else:
    print('Sua categoria é MASTER')
