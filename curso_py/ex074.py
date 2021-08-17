def leianum(msg):
    num = input(msg)
    try:
        float(num)
        print(f'O número que digitou é {num}!')
    except:
        print(f'\033[0;30;41mERRO! O que digitou não é um número!\033[m')


leianum('Digite algo: ')
