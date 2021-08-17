validacao = str(input('Digite o seu sexo(m/f): ').strip().lower()[0])
while validacao not in 'mf':
    print('Digite novamente!')
    validacao = str(input().strip().lower()[0])
print('Cadastro validado com sucesso!')
