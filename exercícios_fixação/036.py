'''
 Um programa de vida saudável quer dar pontos atividades físicas que podem
ser trocados por dinheiro. O sistema funciona assim:
 - Cada hora de atividade física no mês vale pontos
 - até 10h de atividade no mês: ganha 2 pontos por hora
 - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
 - acima de 20h de atividade no mês: ganha 10 pontos por hora
 - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
Faça um programa que leia quantas horas de atividade uma pessoa teve por mês,
calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.
'''
horas = int(input('Quantas horas de atividade por dia você teve por mês? '))

if horas < 10 :
    pontos = horas * 2 
    print(f'Você obteve R${0.05*pontos} por esses exercícios.')
elif 10 <= horas <= 20:
    pontos = horas * 5 
    print(f'Você obteve R${0.05*pontos} por esses exercícios.')
elif horas > 20:
    pontos = horas * 10
    print(f'Você obteve R${0.05*pontos} por esses exercícios.')

