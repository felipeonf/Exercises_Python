palavras = ('teoria','pratica','aprendizado','dedicar','profissionalizar','emprego','futuro')
vogais = ('a','e','i','o','u')
for elemento in palavras:
    print(f'Na palavra {elemento.upper()} temos',end =' ')
    for vogal in vogais:
        if vogal in elemento:
            print(f'{vogal}',end=' ')
    print()
    