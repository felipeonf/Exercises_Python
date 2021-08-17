def menu():
    '''Mostra o menu de opções e retorna a selecionada'''
    opções = {'1' : 'Cadastra aluno',
              '2' : 'Entrada de notas',
              '3' : 'Dados do aluno',
              '4' : 'Extrato geral'}
    while True:
        print('\n ### APC ###\n Opções:')
        for opção,descrição in sorted(opções.items()):
            print(f'{opção} - {descrição}')
        opção = input('\n Digite o número da opção desejada: ')
        if opção in opções:
            return opção
def efetua_cadastro(cadastro):
    ''' Obtém os dados de um aluno e atualiza o cadastro'''
    matricula = input('Digite sua matrícula na UnB: ')
    registra = True
    if matricula in cadastro:
        registro = cadastro[matricula]
        if input(f'{registro["nome"]} já está cadastrado.\n'
                 'Você deseja sobrescrever o registro (sim/não):') == 'não':
            registra = False
    if registra:
        cadastro[matricula] = {'nome' : input('Digite o seu nome completo: '),
                               'listas' : [0.0] * NUM_LISTAS,
                               'projetos' : [0.0] * NUM_PROJETOS}
def entrada_notas(cadastro):
    ''' Busca um aluno no cadastro e obtém as notas das listas e projetos. '''
    if cadastro:
        matricula = input('Buscar pela matrícula: ')
        if matricula in cadastro:
            registro =  cadastro[matricula]
            print(f'Entre com as notas de {registro["nome"]}:')
            registro['listas'] = [float(input(f'Lista {nota_le+1}: '))
                                  for nota_le in range(NUM_LISTAS)]
            registro['projetos'] = [float(input(f'Projeto {nota_p+1}: '))
                                    for nota_p in range(NUM_PROJETOS)] 
        else:
            print(f'A matrícula {matricula} não foi encontrada.')   
    else:
        print('Você precisa cadastrar um aluno primeiro')    
def registro(cadastro):
    ''' Busca um aluno no cadastro e imprime seus dados.'''
    if cadastro:
        matricula = input('Buscar pela matrícula: ')
        if matricula in cadastro:
            imprime_registro(matricula , cadastro[matricula])
        else:
            print(f'A matrícula {matricula} não foi encontrada')
    else:
        print('Você preisa cadastrar um aluno primeiro')
def imprime_registro(matricula,registro):
    ''' Imprime os dados de um aluno.'''
    aluno = f" {matricula} - {registro['nome']}"
    print('#' * (len(aluno)+4))
    print(f'# {aluno} #')
    print('#' * (len(aluno)+4))
    for i,nota_le in enumerate(registro['listas']):
        print(f'Lista {i+1} \t({nota_le:.1f})')
    for i,nota_p in enumerate(registro['projetos']):
        print(f'Projeto {i+1} \t({nota_p:.1f})')
def extrato(cadastro):
    '''Mostra todas as notas, as médias e a nota final de cada aluno.'''
    for matricula in cadastro:
        registro = cadastro[matricula]
        imprime_registro(matricula,registro)
        media_le = media(registro['listas'])
        media_p = media(registro['projetos'])
        n_final = nota_final(media_le,media_p)
        print(f'Listas de Exercícios = {media_le:.1f}')
        print(f'Projetos = {media_p:.1f}')
        print(f'Nota final = {n_final:.1f}')    
def media(lista):
    '''Retorna a media dos valores na lista'''
    return sum(lista)/ len(lista)
def nota_final(nota_le,nota_p):
    ''' Retorna a nota final de APC
    NF = 40% LE + 60% P , se LE e P >= 5.0, senão NF máxima é 4.9
    '''
    nota_final = (0.4 * nota_le) + (0.6 * nota_p)
    if nota_le < 5.0  or nota_p < 5.0:
        nota_final = min(nota_final,4.9)
    
    return nota_final
        
        
#CTE GLOBAIS
NUM_LISTAS = 11
NUM_PROJETOS = 3
#INÍCIO DO PROGRAMA
cadastro = {}
continua = 'sim'
while continua != 'não':
    op = menu()
    if op == '1':
        efetua_cadastro(cadastro)
    elif op == '2':
        entrada_notas(cadastro)
    elif op == '3':
        registro(cadastro)
    elif op == '4':
        extrato(cadastro)
    continua = input('Deseja continuar? (sim/não)')
