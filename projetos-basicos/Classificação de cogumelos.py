# METODOS
def calcula_media(linha):
    return sum(linha)/len(linha)
def calcula_var(atributo,media,size):
    return (atributo - media)**2/ size  
def calcula_dp(variancia):
    return variancia ** 0.5
def normaliza(elemento, media, desvio_padrao):
    return (elemento - media) /desvio_padrao


# ENTRADA DE DADOS TREINAMENTO
K = int(input())
Ntrain,Ntest = (int(x) for x in input().split())
if K>0 and K%2 != 0 and Ntrain>0 and Ntest>0 :
    Xtrain = []
    for elemento in range(Ntrain):
        values = input().split()
        mushroom = dict(cap_shape=values [0] , cap_surface= values[1], cap_color= values[2], bruises= values[3], odor= values[4]
                        ,gill_attachment= values[5], gill_spacing=values[6], gill_size=values[7], gill_color=values[8],
                        stalk_shape=values[9], stalk_root=values[10], stalk_surface_above_ring=values[11],
                        stalk_surface_below_ring= values[12], stalk_color_above_ring=values[13],
                        stalk_color_below_ring=values[14], veil_type=values[15], veil_color=values[16], ring_number=values[17],
                        ring_type= values[18],
                        spore_print_color=values[19], population=values[20], habitat=values[21])
        Xtrain.append(mushroom)
# SET NOS ATRIBUTOS
atributos =[ dict(name = 'cap_shape', lst_strg =['b','c','x','f','k','s'], lst_int = [0,1,2,3,4,5]), 
dict(name = 'cap_surface' , lst_strg =['f','g','y','s'], lst_int = [0,1,2,3]),     
dict(name = 'cap_color', lst_strg =['n','b','c','g','r','p','u','e','w','y'], lst_int = [0,1,2,3,4,5,6,7,8,9]),    
dict(name = 'bruises', lst_strg =['t','f'], lst_int = [0,1]),      
dict(name = 'odor', lst_strg =['a','l','c','y','f','m','n','p','s'], lst_int = [0,1,2,3,4,5,6,7,8]),      
dict(name = 'gill_attachment', lst_strg =['a','d','f','n'], lst_int = [0,1,2,3]),       
dict(name = 'gill_spacing', lst_strg =['c','w','d'], lst_int = [0,1,2]),      
dict(name = 'gill_size', lst_strg =['b','n'], lst_int = [0,1]),       
dict(name = 'gill_color', lst_strg =['k','n','b','h','g','r','o','p','u','e','w','y'], lst_int = [0,1,2,3,4,5,6,7,8,9,10,11]),       
dict(name = 'stalk_shape', lst_strg =['e','t'], lst_int = [0,1]),          
dict(name = 'stalk_root', lst_strg =['b','c','u','e','z','r','?'], lst_int = [0,1,2,3,4,5,6]),           
dict(name = 'stalk_surface_above_ring', lst_strg =['f','y','k','s'], lst_int = [0,1,2,3]),         
dict(name = 'stalk_surface_below_ring', lst_strg =['f','y','k','s'], lst_int = [0,1,2,3]),          
dict(name = 'stalk_color_above_ring', lst_strg =['n','b','c','g','o','p','e','w','y'], lst_int = [0,1,2,3,4,5,6,7,8]),          
dict(name = 'stalk_color_below_ring', lst_strg =['n','b','c','g','o','p','e','w','y'], lst_int = [0,1,2,3,4,5,6,7,8]),          
dict(name = 'veil_type', lst_strg =['p','u'], lst_int = [0,1]),           
dict(name = 'veil_color', lst_strg =['n','o','w','y'], lst_int = [0,1,2,3]),         
dict(name = 'ring_number', lst_strg =['n','o','t'], lst_int = [0,1,2]),          
dict(name = 'ring_type', lst_strg =['c','e','f','l','n','p','s','z'], lst_int = [0,1,2,3,4,5,6,7]),          
dict(name = 'spore_print_color', lst_strg =['k','n','b','h','r','o','u','w','y'], lst_int = [0,1,2,3,4,5,6,7,8]),         
dict(name = 'population', lst_strg =['a','c','n','s','v','y'], lst_int = [0,1,2,3,4,5]),           
dict(name = 'habitat', lst_strg =['g','l','m','p','u','w','d'], lst_int = [0,1,2,3,4,5,6])]
# FORMANDO PARA INTEIRO
lista_inteiro = []
for cogumelo in Xtrain:
    lista_cogumelo = []
    for atributo in atributos:
        lista_cogumelo.append(atributo['lst_int'][atributo['lst_strg'].index(cogumelo[atributo['name']])])
    lista_inteiro.append(lista_cogumelo)
# TRANSFORMAÇÃO EM COLUNAS
lista_colunas = []
j= 0
while True:
    lista_atributos = []
    for linha in range(Ntrain):
        elemento = lista_inteiro[linha][j]
        lista_atributos.append(elemento)  
    lista_colunas.append(lista_atributos)    
    if j < 21:
        j+=1
    else:
        break
#NORMALIZACAO DOS ATRIBUTOS
lista_dp = []
medias = []
lista_variancias = []
# calculando medias
for atributo in lista_colunas:
    media = calcula_media(atributo)
    medias.append(media)
    lista_var= []
# calculando variancias
    for elemento in atributo:
        variancia = (elemento - media)**2
        lista_var.append(variancia)
    variancia_completa = sum(lista_var)/ len(lista_var)
    lista_variancias.append(variancia_completa)
#calculando desvios padrao
    desvio_padrao = variancia_completa ** 0.5
    lista_dp.append(desvio_padrao)
# normalizacao treinamento
lista_normalizada_treinamento = []
i = 0
for atributo in lista_colunas:
    desvio_padrao = lista_dp[i]
    media = medias [i]
    lista_atributo_normalizado = []
    for elemento in atributo:
        if desvio_padrao == 0:
            lista_atributo_normalizado.append(0)
        else:
            atributo_normalizado = normaliza(elemento,media,desvio_padrao)
            lista_atributo_normalizado.append(atributo_normalizado) 
    lista_normalizada_treinamento.append(lista_atributo_normalizado)
    i +=1
# LEITURA DOS ROTULOS DE TREINAMENTO
rotulos_treinamento = []
aux = Ntrain
while aux > 0:
    aux -=1
    rotulos_treinamento.append(input())
#ENTRADA DE DADOS DE TESTE
Xtest = []
for elemento in range(Ntest):
    values = input().split()
    mushroom = dict(cap_shape=values [0] , cap_surface= values[1], cap_color= values[2], bruises= values[3], odor= values[4],gill_attachment= values[5], gill_spacing=values[6], gill_size=values[7], gill_color=values[8],
                         stalk_shape=values[9], stalk_root=values[10], stalk_surface_above_ring=values[11],
                          stalk_surface_below_ring= values[12], stalk_color_above_ring=values[13],
                        stalk_color_below_ring=values[14], veil_type=values[15], veil_color=values[16], ring_number=values[17],
                          ring_type= values[18],
                         spore_print_color=values[19], population=values[20], habitat=values[21]) 
    Xtest.append(mushroom)
 #LISTA INTEIRO TESTE
lista_inteiro_teste = []
for cogumelo in Xtest:
    lista_cogumelo_teste = []
    for atributo in atributos:
        lista_cogumelo_teste.append(atributo['lst_int'][atributo['lst_strg'].index(cogumelo[atributo['name']])])
    lista_inteiro_teste.append(lista_cogumelo_teste)
 #NORMALIZACAO TESTE
 # TRANSFORMAÇÃO EM COLUNAS TESTE
lista_colunas_teste = []
l= 0
while True:
    lista_atributos_teste = []
    for linha in range(Ntest):
        elemento = lista_inteiro_teste[linha][l]
        lista_atributos_teste.append(elemento)
    lista_colunas_teste.append(lista_atributos_teste)    
    if l < 21:
        l+=1
    else:
        break
# NORMALIZAÇÃO DOS ATRIBUTOS DE TESTE
lista_normalizada_teste = []
i = 0
for atributo in lista_colunas_teste:
    desvio_padrao = lista_dp[i]
    media = medias [i]
    atributo_teste = []
    for elemento in atributo:
        if desvio_padrao == 0:
            atributo_teste.append(0)
        else:
            atributo_normalizado = normaliza(elemento,media,desvio_padrao)
            atributo_teste.append(atributo_normalizado)
    lista_normalizada_teste.append(atributo_teste)
    i +=1
#DISTANCIAS
lista_treinamento = []
for atributo in range(0,Ntrain):
    lista_cogumelos_treinamento = []
    for coluna in range(0,22):
        elemento = lista_normalizada_treinamento [coluna][atributo]
        lista_cogumelos_treinamento.append(elemento)
    lista_treinamento.append(lista_cogumelos_treinamento)
lista_teste = []
for atributo in range(0,Ntest):
    lista_cogumelos_teste = []
    for coluna in range(0,22):
        elemento = lista_normalizada_teste [coluna][atributo]
        lista_cogumelos_teste.append(elemento)    
    lista_teste.append(lista_cogumelos_teste)
for cogumelo_teste in lista_teste:
    distance = []
    for cogumelo_treinamento in lista_treinamento:
        add = 0
        for y in range (0, 22):
            add_distance = (cogumelo_teste[y] - cogumelo_treinamento[y] )**2
            add += add_distance
        distancias = add ** 0.5
        distance.append(distancias)
    menores_distancias = sorted(range(len(distance)), key = lambda sub: distance[sub])[:K]
    e = 0
    p = 0
    for elemento in menores_distancias:
        if rotulos_treinamento[elemento] == 'e':
            e += 1
        else:
            p +=1
    if e > p:
        print('e')
    else:
        print('p')
    