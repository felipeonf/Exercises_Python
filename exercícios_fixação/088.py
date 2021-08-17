'''Crie um programa que melhore o procedimento Gerador() da questão anterior
para que mostre uma mensagem vário
Ex: Ao chamar Gerador("Aprendendo Algoritmos", 4) aparece:
+-------=======------+
 Aprendendo Algoritmos
 Aprendendo Algoritmos
 Aprendendo Algoritmos
 Aprendendo Algoritmos
+-------=======------+ '''
def Gerador(mensagem,repeticoes):
    print('>>>{}>'.format('-'*(len(mensagem)+5)))
    while repeticoes > 0:
         print('    ',mensagem)
         repeticoes -= 1
    print('>>>{}>'.format('-'*(len(mensagem)+5)))
mensagem = input('Digite uma mensagem: ')
repeticoes = int(input('Digite as repetições: '))
Gerador(mensagem,repeticoes)