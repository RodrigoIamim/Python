from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [1] somar  
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair ''')
    print('-=-'*12)
    opção = int(input('-->'*2 + 'Qual opção você escolhe? '))
    if opção == 1:
        soma = n1 + n2
        print('{} + {} vale {}'.format(n1, n2, soma))
    elif opção == 2:
        mult = n1 * n2
        print('{} x {} vale {}'.format(n1, n2, mult))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        elif n2 > n1:
            maior = n2
        print('Entre {} e {}, {} é maior'.format(n1, n2, maior))
    elif opção == 4:
        print('insira novos valores')
        n1 = float(input('Primeiro: '))
        n2 = float(input('Segundo: '))
    elif opção == 5:
        print('Você escolheu sair do programa.')
    else:
        print('\033[31m opção inválida! tente novamente\033[m')
    sleep(1.5)
print('Fim')
