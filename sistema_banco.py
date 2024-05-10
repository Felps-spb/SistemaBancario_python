
menu = print('''

    *****SISTEMA BANCARIO(BANCO DO BRASIL)*****
            escolha uma opção de ação:

    (d)- deposito
    (s)- saque
    (e)- extrato
    (q)- sair

        obrigado pela sua escolha de banco!


''')

saldo = 0
limite = 500
extrato = ""
limite_saque = 0
LIMITE_SAQUE = 3
while True:

    opcao = input(menu)

    if opcao == "d":

            print("qual o valor que vc deseja depositar?: R$")
            deposito = float(input())

            if deposito < 0:
                print("valor invalido!!, tente novamente")

            else:    
                saldo += deposito
                extrato += f"deposito: R$ {deposito:.2f}\n"

                while True:
                    print("deseja depositar outro valor ? s/n")
                    opcao = input()

                    if opcao == 's':
                        print("qual o valor que vc deseja depositar?: R$")
                        deposito = float(input())
                        saldo += deposito
                        extrato += f"deposito: R$ {deposito:.2f}\n"

                    elif opcao == 'n':
                        break

    if opcao == "s":
            if limite_saque == LIMITE_SAQUE:
                print("voce atingiu o limite diario de saque")
             
            else:
                print("qual o valor que vc deseja sacar(limite de R$500,00): R$")
                saque = float(input())

                if saque > 500:
                    print("valor invalido, tente novamente")
                elif saque > saldo:
                    print("saldo insuficiente, tente novamente")   
                else:
                    saldo -= saque
                    limite_saque += 1
                    extrato += f"saque: R$ {saque:.2f}\n"

        
    if opcao == "e":
        print("\n================EXTRATO================")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=======================================")


    if opcao == "q":
        print("programa finalizado com sucesso!")   
        break     