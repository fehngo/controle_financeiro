from time import sleep

from v1_json import funcoes

while True:
    opcao = funcoes.menu(
        "Adicionar Transações",
        "Listar Transações",
        "Mostrar Saldo",
        "Filtrar Transações",
        "Excluir Transações",
        "Sair",
    )

    if opcao == 1:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Adicionar Transações")
        dicionario = {}
        dicionario["descricao"] = input("Digite uma descrição da transação: ").strip().capitalize()
        dicionario["valor"] = funcoes.leia_float("Digite o valor da transação: ")
        while True:
            dicionario["tipo"] = (
                input("Digite o tipo da transação (Entrada/Saida): ").strip().capitalize()
            )
            if dicionario["tipo"] in ("Entrada", "Saida"):
                break
            else:
                print('Digite apenas "Entrada" ou "Saida".')
        lista.append(dicionario)
        funcoes.salva_banco(lista)
        print("")
        sleep(2)

    elif opcao == 2:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Listar Transações")
        funcoes.listar_transacoes(lista)
        print("")
        sleep(2)

    elif opcao == 3:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Saldo Atual")
        saldo = funcoes.calcula_saldo(lista)
        if saldo >= 0:
            print(f"\033[32mO saldo atual da sua conta é: R$ {saldo:.2f}\033[m")
        else:
            print(f"\033[31mO saldo atual da sua conta é: R$ {saldo:.2f}\033[m")

    elif opcao == 4:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Filtrar Transações")
        while True:
            resposta = (
                input('Você deseja filtrar transações de "Entrada" ou "Saida"?: ')
                .strip()
                .capitalize()
            )
            if resposta in ("Entrada", "Saida"):
                break
            else:
                print('Digite apenas "Entrada" ou "Saida".')
        print("")
        funcoes.filtrar_transacoes(lista, resposta)
        print("")
        sleep(2)

    elif opcao == 5:
        lista = funcoes.carrega_banco()
        while True:
            funcoes.cabecalho("Excluir Transação")
            funcoes.listar_transacoes(lista)
            resposta = funcoes.leia_int("Qual o número da transação que você deseja remover?: ")
            if 0 < resposta <= len(lista):
                del lista[resposta - 1]
                print("Transação removida com sucesso.")
                break
            else:
                print("Número da transação inválido.")
                print("")
                sleep(2)
        funcoes.salva_banco(lista)
        print("")
        sleep(2)

    elif opcao == 6:
        print("Saindo do programa...")
        sleep(2)
        break
        break
