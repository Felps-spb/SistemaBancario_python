#menu do sistema bancario

def menu():
 menu = '''

    *****SISTEMA BANCARIO(BANCO DO BRASIL)*****
            escolha uma opção de ação:

    [d]-\tdeposito
    [s]-\tsaque
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [e]-\textrato
    [q]-\tsair

        obrigado pela sua escolha de banco!

    => '''
 return input(menu)

#DEPOSITO:
def deposito (saldo,extrato,valor,/):
    if valor > 0:
        saldo += valor
        print("**** deposito realizado com sucesso!!! ****")
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
    else:
        print("ERRO: digite um valor valido!!!")

    while True:
        print("deseja depositar outro valor ? s/n")
        opcao = input()

        if opcao == 's':
            print("digite o valor a ser depositado R$: ")
            deposito = float(input())
            print("**** deposito realizado com sucesso!!! ****")
            saldo += deposito
            extrato += f"Depósito:\tR$ {valor:.2f}\n"

        elif opcao == 'n':
            break

    return saldo, extrato      

#SAQUE:
def saque(*,saldo,extrato,valor,limite_saque,saque_limitante,limite):
    
    saque_maior = valor > saldo
    saque_limite = valor > limite
    numero_saque = limite_saque >= saque_limitante

    if saque_maior:
        print("ERRO: Valor de saque maior que saldo")

    elif saque_limite:
        print("ERRO: Valor de saque superior ao limite")

    elif numero_saque:
        print("ERRO: voce atingiu o limite de saque diario")

    else:
        saldo -= valor
        print("**** Saque realizado com sucesso!!! ****")
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        limite_saque += 1
    
    return saldo, extrato    

#EXTRATO:
def exibir_extrato(saldo,/,*,extrato):

    print("\n================EXTRATO================")
    print("Nao foram realizadas movimentacoes." if not extrato else extrato)
    print(f"\nsaldo: R$ {saldo:.2f}")
    print("=======================================")

#NOVA CONTA
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    else:
        nome= input("informe o seu nome: ")
        data_nascimento= input("informe sua data de nascimento (dia-mes-ano): ")
        endereco= input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        usuarios.append({"nome":nome, "data_nascimento":data_nascimento, "cpf":cpf, "endereco":endereco })
        print("=== Usuário criado com sucesso! ===")

#FILTRO DE USUARIO
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

#CRIAR CONTA
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
#LISTA DE CONTAS
def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():

    AGENCIA = "0001"


    saldo = 0
    extrato =''
    limite = 500
    limite_saque = 0
    LIMITE_SAQUE = 3
    usuarios = []
    contas = []
    while True:

        escolha = menu()

        if escolha == "d":
           valor = float(input("digite o valor a ser depositado R$: "))
           saldo, extrato = deposito(saldo,extrato,valor)

        elif escolha == "s":
            valor = float(input("digite o valor a ser sacado R$: "))
            saldo, extrato = saque(
                saldo = saldo
                ,extrato = extrato
                ,valor = valor
                ,limite_saque = limite_saque
                ,saque_limitante = LIMITE_SAQUE
                ,limite = limite
                )

        elif escolha == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        
        elif escolha == "lc":
            lista_contas(contas)

        elif escolha == "nu":
            criar_usuario(usuarios)

        elif escolha == "e":
            exibir_extrato(saldo, extrato = extrato)
    
        elif escolha == "q":
            break
    

main()