#Crie um programa que leia o número de dias trabalhados em um mês e mostre o
#salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
def calculaSalario(d,c,p):
    return d*c*p
diasTrabalhados = int(input('Quantos dias você trabalhou? '))
cargaHoraria = 8.0
precoHora = 25.0
print(f'O seu salário com {diasTrabalhados} dias trabalhados, a carga horária de {cargaHoraria} horas por dia e o preço da hora sendo {precoHora} será de R${calculaSalario(diasTrabalhados,cargaHoraria,precoHora)}')



