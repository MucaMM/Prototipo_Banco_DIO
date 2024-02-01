cont = 0
conta = 0
dep = []
saq = []
soma = 0
sub = 0


while True:
    print('[d] Depositar\n'
          '[s] Sacar\n'
          '[e] extrato\n'
          '[m] Sair\n')

    escolha = input("Escolha uma das opções: \n\n=>")
    
    if escolha == 'd':
        while True:
            deposito = float(input('Valor: \n'))
            if deposito <= 0:
                print('Apenas valores positivos!')
                break
            elif deposito > 0:
                dep.append(deposito)
                soma = sum(dep)
                break
            else:
                break

    if escolha == 's':
        while True:
            saque = float(input('Insira o valor desejado de saque: '))
            cont += 1
            if saque <= 0 or saque > 500:
                print('Valor fora do permitido!')
                break
            elif conta <= 0:
                print('Conta sem saldo suficiente.')
                break
            elif cont > 3:
                print('Número de saques diario excedido!\n')
                break
            elif saque > 0 or saque < 500:
                saq.append(saque)
                sub = sum(saq)
                break
            else:
                break

    conta =  soma - sub
    so = soma
    su = sub

    if escolha == 'e': 
        print(f'DEPOSITO: R$ {so:.2f}\nSAQUE: R$ {su:.2f}\nSALDO: R$ {conta:.2f}\n')   

    if conta == 0:
        print(f'Não houve transações!\nSALDO: R$ {conta:.2f}\n')
    if escolha == 'm':
        break
    





