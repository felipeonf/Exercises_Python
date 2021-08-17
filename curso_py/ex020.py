soma = 0
count = 0
for num in range(1,500):
    if num % 2 != 0 and num % 3 == 0:
        count += 1
        soma += num
print(f'A soma dos {count} números ímpares e múltiplos de três entre 1 e 500 é {soma}')

