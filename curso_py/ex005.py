number = int(input('Digite um número: '))
u = number // 1 % 10
d = number // 10 % 10
c = number // 100 % 10
m = number // 1000 % 10

print(f'Vamos analisar o número {number}')
print(f'Unidade : {u}')
print(f'Dezena : {d}')
print(f'Centena : {c}')
print(f'Milhar : {m}')