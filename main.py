from time import sleep
import funcoes

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

    if opcao == 2:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Listar Transações")
        funcoes.listar_transacoes(lista)
        print("")
        sleep(2)

    if opcao == 3:
        lista = funcoes.carrega_banco()
        funcoes.cabecalho("Saldo Atual")
        saldo = funcoes.calcula_saldo(lista)
        if saldo >= 0:
            print(f"\033[32mO saldo atual da sua conta é: R$ {saldo:.2f}\033[m")
        else:
            print(f"\033[31mO saldo atual da sua conta é: R$ {saldo:.2f}\033[m")
