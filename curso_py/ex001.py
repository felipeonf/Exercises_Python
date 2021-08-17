#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações sobre ele

variavel = input('Digite algo: ')

print('O tipo primitivo desse valor é',type(variavel))
# todo input retorna uma string
print('Só tem espaços?', variavel.isspace())
print('É um número?', variavel.isnumeric())
print('É alfabético?', variavel.isalpha())
print('É alfanumérico?', variavel.isalnum())
print('Está em maiúsculo?', variavel.isupper())
print('Está em minúsculo?', variavel.islower())
print('Está capitalizada?', variavel.istitle())
