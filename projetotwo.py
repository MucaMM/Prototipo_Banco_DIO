import re


menu = """

[d]  Depositar
[s]  Sacar
[e]  Extrato
[c]  Cadastrar cliente
[mc] Mostrar clientes cadastrados
[cc] Cadastrar conta
[mm] Mostrar conta cadastrada
[q]  Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientess = []
contas = []


def deposito(): 
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

def saque():
    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")

def extratos():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastro(clientes):
    # capta os dados do cliente p/ cadastro
    nome = input('Nome: ')
    nascimento = input('Data de nascimento: ')
    cpf = input('CPF: ')

    cpf = re.sub(r'\D', '', cpf)

    # verifica se o CPF ja foi cadastrato
    for cliente in clientes:
        if cliente['cpf'] == cpf:
            print('CPF ja cadastrado')
            return

    endereço = input('Endereço =>\nLoagradouro: '), input('Nº: '), input('Bairro: '), input('Cidade/Estado: ')

    # adc os dados em um dicionario
    novo_cliente = {
        'nome': nome,
        'nascimento': nascimento,
        'cpf': cpf,
        'endereço': endereço
    }

    # adc os dados do dicionario na lista (clientes)
    clientes.append(novo_cliente)

def mostrar_clientes():
    for cli in clientess:
        for titulo, resp in cli.items():
            print((titulo) + ': ' + str(resp)) 

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cadastro_conta(contas, usuarios):
    conta = len(contas) + 1
    agencia = '0001'
    cpf = input('A qual cpf a conta deve ser vinculada? ')

    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print('conta criada')

    nova_conta = {
        'conta': conta,
        'agencia': agencia,
        'usuario': cpf
    }

    contas.append(nova_conta)

def mostrar_conta():
    for cont in contas:
        for pri, secu in cont.items():
            print((pri) + ': ' + str(secu))


while True:

    opcao = input(menu)

    if opcao == "d":
        print(deposito())

    elif opcao == "s":
        print(saque())

    elif opcao == "e":
        print(extratos())

    elif opcao == "c":
        cadastro(clientess)

    elif opcao == 'mc':
        mostrar_clientes()

    elif opcao == 'cc':
        cadastro_conta(contas)

    elif opcao == 'mm':
        mostrar_conta()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")