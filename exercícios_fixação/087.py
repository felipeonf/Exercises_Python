'''Crie um programa que melhore o procedimento Gerador() da questão anterior
para que mostre uma mensagem personalizada, passada como parâmetro.
Ex: Ao chamar Gerador("Aprendendo Portugol") aparece:
+-------=======------+
 Aprendendo Algoritmos
+-------=======------+'''
def Gerador(mensagem):
    print('''>>>{}>
    {}
>>>{}>'''.format('-'*(len(mensagem)+5),mensagem,'-'*(len(mensagem)+5)))
mensagem = input('Digite uma mensagem: ')
Gerador(mensagem)