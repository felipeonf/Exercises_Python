def voto(ano):
    from datetime import datetime
    ano_atual = datetime.now().year
    idade = ano_atual - ano
    if idade < 16:
        print(f'Com {idade} anos você não precisa votar ainda')
    elif 16 <= idade < 18:
        print(f'Com {idade} anos você possui o voto FACULTATIVO!')
    else:
        print(f'Com {idade} anos você possui o voto OBRIGATÓRIO!')

print('-'*30)
ano_nascimento = int(input("Digite o ano do seu nascimento: "))
voto(ano_nascimento)