from time import sleep
import json

arq = "banco.json"


def cabecalho(msg):
    print("-" * 70)
    print(msg.center(70))
    print("-" * 70)


def leia_int(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print("Digite apenas numeros inteiros")


def leia_float(msg):
    while True:
        try:
            return float(input(msg))
        except ValueError:
            print("Digite apenas numeros válidos")


def carrega_banco():
    try:
        with open(arq, "r", encoding="utf-8") as banco:
            return json.load(banco)

    except (FileNotFoundError, json.JSONDecodeError):
        with open(arq, "w", encoding="utf-8") as banco:
            json.dump([], banco, ensure_ascii=False, indent=4)
        return []


def salva_banco(lista):
    try:
        with open(arq, "w", encoding="utf-8") as banco:
            json.dump(lista, banco, ensure_ascii=False, indent=4)
    except Exception:
        print("Ocorreu um erro inesperado.")


def menu(*funcoes):
    while True:
        cabecalho("Sistema Financeiro FNC")
        for i, v in enumerate(funcoes):
            print(f"{i+1} - {v}")
        print("")
        resposta = leia_int("Digite a opção desejada: ")
        sleep(2)
        if 0 < resposta <= len(funcoes):
            print("")
            return resposta
        else:
            print(f"Digite um numero inteiro entre 1 e {len(funcoes)}")


def listar_transacoes(lista):
    print(f'{"ind":^5}|{"Descrição":<48}|{"R$ Valor":^15}')
    print("-" * 70)
    for i, v in enumerate(lista):
        if v["tipo"] == "Entrada":
            print(f"\033[32m{i+1:^5}|{v['descricao']:<48}|{f'R$ {v['valor']:.2f}':^15}\033[m")
        else:
            print(f"\033[31m{i+1:^5}|{v['descricao']:<48}|{f'R$ {v['valor']:.2f}':^15}\033[m")
    print("-" * 70)
    saldo = calcula_saldo(lista)
    if saldo >= 0:
        print(f"\033[32m{'TOTAL':^54}| {f'R$ {saldo:.2f}':^15}\033[m")
    else:
        print(f"\033[31m{'TOTAL':^54}| {f'R$ {saldo:.2f}':^15}\033[m")


def calcula_saldo(lista, filtro="Total"):
    saldo = 0
    for v in lista:
        tipo = v["tipo"]
        if filtro == "Entrada" and tipo == "Entrada":
            saldo += v["valor"]
        elif filtro == "Saida" and tipo == "Saida":
            saldo += v["valor"]
        elif filtro == "Total":
            if tipo == "Entrada":
                saldo += v["valor"]
            else:
                saldo -= v["valor"]
    return saldo


def filtrar_transacoes(lista, filtro):
    cabecalho("Filtrar Transações")
    encontrou = False
    print(f'{"ind":^5}|{"Descrição":<48}|{"R$ Valor":^15}')
    print("-" * 70)
    for i, v in enumerate(lista):
        if filtro == "Entrada":
            if v["tipo"] == "Entrada":
                print(f"\033[32m{i+1:^5}|{v['descricao']:<48}|{f'R$ {v['valor']:.2f}':^15}\033[m")
                encontrou = True
        else:
            if v["tipo"] == "Saida":
                print(f"\033[31m{i+1:^5}|{v['descricao']:<48}|{f'R$ {v['valor']:.2f}':^15}\033[m")
                encontrou = True
    print("")
    if not encontrou:
        print(f"{'Nenhuma transação encontrada.'}".center(70))

    print("-" * 70)
    saldo = calcula_saldo(lista, filtro)
    if filtro == "Entrada":
        print(f"\033[32m{f'Total do filtro de {filtro}':^54}| {f'R$ {saldo:.2f}':^15}\033[m")
    else:
        print(f"\033[31m{f'Total do filtro de {filtro}':^54}| {f'R$ {saldo:.2f}':^15}\033[m")
