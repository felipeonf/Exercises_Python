#[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
#fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
#quantos dias de vida um fumante perderá e exiba o total em dias.
def calculaTotalc(anos,dias):
    # cada ano possui 365 dias, a quantidade de cigarros por dia será multiplicada pelo número de dias por ano, 
    # entao será 365 * qtde de anos * qtde de cigarros.
    return 365 * qtdediaCigarros * qtdeAnosfumados
def calculaDiasp(m,total):
    minutosTotais = m * total
    diasPerdidos = minutosTotais / 1440
    return diasPerdidos


qtdediaCigarros, qtdeAnosfumados = (int(x) for x in input('Quantos cigarros você fuma por dia e há quantos anos você fuma? ').split())


qtdetotalCigarros = calculaTotalc(qtdediaCigarros,qtdeAnosfumados)

print(f'Se você fumou {qtdediaCigarros} cigarros por dia durante {qtdeAnosfumados} anos, já perdeu {int(calculaDiasp(10,qtdetotalCigarros))} dias de vida. ')

