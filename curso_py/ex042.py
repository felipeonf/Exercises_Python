tupla = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze',
'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
numero = int(input('Digite um número entre 0 e 20: '))
if numero > 20 or numero < 0:
    while numero > 20 or numero < 0:
        numero = int(input('Número inválido,tente novamente!. Digite um número entre 0 e 20: '))
objetos = tuple(enumerate(tupla))
for elemento in objetos:
    if numero in elemento:
        print(elemento[1])
        break
