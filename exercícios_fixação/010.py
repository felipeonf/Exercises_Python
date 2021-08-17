# Faça um algoritmo que leia a largura e altura de uma parede, calcule e
#mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

def calculaArea(largura,altura):
    area = largura * altura 
    return area

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
litroTinta = float(input('Quantos m² 1 litro de tinta pode pintar? '))
print(f'{calculaArea(largura,altura)}m².')
print(f'Serão necessários {calculaArea(largura,altura)*litroTinta} litros de tinta para pintar a parede.')




