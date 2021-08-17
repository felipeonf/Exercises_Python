#maioridade
from datetime import date
anoatual = date.today().year
contm = 0
contn = 0
for data in range(1,7+1):
    ano = int(input('Qual foi o ano do seu nascimento? '))
    idade = anoatual - ano
    if idade >= 21:
        contm += 1
    else:
        contn += 1
print(f'{contm} pessoas já atingiram a maioridade e {contn} ainda não atingiram.')
