#Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
a,b,c = (int(x) for x in input('Digite o valor de a, b e c: ').split())
delta = (b**2) - (4*a*c)
print(f'A equação {a}x² + {b}x + {c} possui como valor de delta {delta}.')
