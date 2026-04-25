from sqlalchemy import func

from v2_sqlalchemy.database.connection import Base, engine, session
from v2_sqlalchemy.models.categoria import Categoria  # noqa
from v2_sqlalchemy.models.transacao import Transacao  # noqa

Base.metadata.create_all(bind=engine)

# Cat = [
#     Categoria(categoria="Salario"),
#     Categoria(categoria="Mercado"),
#     Categoria(categoria="Combustivel"),
#     Categoria(categoria="Farmacia"),
#     Categoria(categoria="Lazer"),
#     Categoria(categoria="FastFood"),
#     Categoria(categoria="Outros"),
# ]
# session.add_all(Cat)
# session.commit()

# # categoria_salario = session.query(Categoria).filter_by(categoria="Salario").first()
# # categoria_mercado = session.query(Categoria).filter_by(categoria="Mercado").first()
# # categoria_combustivel = session.query(Categoria).filter_by(categoria="Combustivel").first()
# # categoria_farmacia = session.query(Categoria).filter_by(categoria="Farmacia").first()
# # categoria_lazer = session.query(Categoria).filter_by(categoria="Lazer").first()
# # categoria_fastfood = session.query(Categoria).filter_by(categoria="FastFood").first()
# # categoria_outros = session.query(Categoria).filter_by(categoria="Outros").first()
# categorias = session.query(Categoria).all()
# print(categorias)
# categoria_id = {}
# for c in categorias:
#     categoria_id[c.categoria] = c.id
# # print(categoria_id)

# trans = [
#     Transacao(
#         descricao="Pagamento Janeiro",
#         valor=3500.00,
#         tipo="entrada",
#         data="01-01-2026",
#         categoria_id=categoria_id["Salario"],
#     ),
#     Transacao(
#         descricao="Combustivel ida trabalho",
#         valor=50.00,
#         tipo="saida",
#         data="02-01-2026",
#         categoria_id=categoria_id["Combustivel"],
#     ),
#     Transacao(
#         descricao="Jantar Romantico",
#         valor=127.78,
#         tipo="saida",
#         data="02-01-2026",
#         categoria_id=categoria_id["Mercado"],
#     ),
#     Transacao(
#         descricao="Posto nota 10",
#         valor=50.00,
#         tipo="saida",
#         data="05-01-2026",
#         categoria_id=categoria_id["Combustivel"],
#     ),
#     Transacao(
#         descricao="Remedio Filho",
#         valor=67.41,
#         tipo="saida",
#         data="07-01-2026",
#         categoria_id=categoria_id["Farmacia"],
#     ),
#     Transacao(
#         descricao="Posto nota 10",
#         valor=50.00,
#         tipo="saida",
#         data="07-01-2026",
#         categoria_id=categoria_id["Combustivel"],
#     ),
#     Transacao(
#         descricao="Macarrao Molho Branco",
#         valor=47.29,
#         tipo="saida",
#         data="10-01-2026",
#         categoria_id=categoria_id["Mercado"],
#     ),
#     Transacao(
#         descricao="Posto nota 10",
#         valor=50.00,
#         tipo="saida",
#         data="11-01-2026",
#         categoria_id=categoria_id["Combustivel"],
#     ),
#     Transacao(
#         descricao="Acai Parque",
#         valor=17.00,
#         tipo="saida",
#         data="11-01-2026",
#         categoria_id=categoria_id["Lazer"],
#     ),
#     Transacao(
#         descricao="Pizza noite",
#         valor=54.74,
#         tipo="saida",
#         data="11-01-2026",
#         categoria_id=categoria_id["FastFood"],
#     ),
#     Transacao(
#         descricao="Jogo Videogame",
#         valor=274.78,
#         tipo="saida",
#         data="12-01-2026",
#         categoria_id=categoria_id["Outros"],
#     ),
# ]
# session.add_all(trans)
# session.commit()

# buscar = session.query(Transacao, Categoria).join(Categoria).all()
# for t, c in buscar:
#     print(f"{t.descricao} | {t.valor} | {c.categoria}")

# entrada = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "entrada").scalar()
# print(f"Entrada = {entrada}")
# saida = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "saida").scalar()
# print(f"Saida = {saida}")
# print(f"TOTAL = {entrada - saida}")

# resultado = session.query(Transacao.tipo, func.sum(Transacao.valor)).group_by(Transacao.tipo).all()
# for tipo, valor in resultado:
#     print(f"{tipo} = {valor}")

# resultado2 = (
#     session.query(Categoria.categoria, func.sum(Transacao.valor))
#     .join(Transacao)
#     .group_by(Categoria.categoria)
#     .all()
# )
# for categoria, valor in resultado2:
#     print(f"{categoria} = {valor}")


# Nível 1
# Exercício 1
soma = session.query(func.sum(Transacao.valor)).scalar()
print(f"A soma de todas as transações é: {soma}\n")

# Exercício 2
entrada = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "entrada").scalar()
print(f"A soma de todas entradas foram: {entrada}")
saida = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "saida").scalar()
print(f"A soma de todas saidas foram: {saida}")

resultado = session.query(Transacao.tipo, func.sum(Transacao.valor)).group_by(Transacao.tipo).all()
for tipo, valor in resultado:
    print(f"{tipo} = {valor}")
print("")

# Exercício 3
entrada = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "entrada").scalar()
saida = session.query(func.sum(Transacao.valor)).filter(Transacao.tipo == "saida").scalar()
print(f"O saldo final é: {entrada - saida}\n")

# Nível 2
# Exercício 4
resultado = session.query(Transacao.tipo, func.sum(Transacao.valor)).group_by(Transacao.tipo).all()
for tipo, valor in resultado:
    print(f"{tipo} = {valor}")
print("")

# Exercício 5
resultado = (
    session.query(Transacao.categoria_id, func.sum(Transacao.valor))
    .group_by(Transacao.categoria_id)
    .all()
)
for cat, valor in resultado:
    print(f"{cat} = {valor}")

resultado = (
    session.query(Categoria.categoria, func.sum(Transacao.valor))
    .join(Transacao)
    .group_by(Categoria.categoria)
    .all()
)
for cat, valor in resultado:
    print(f"{cat} = {valor}")
print("")

# Exercício 6
resultado = (
    session.query(Categoria.categoria, func.sum(Transacao.valor))
    .join(Transacao)
    .group_by(Categoria.categoria)
    .filter(Transacao.tipo == "saida")
)
catmaior = ""
valmaior = 0
for cat, valor in resultado:
    if valor > valmaior:
        valmaior = valor
        catmaior = cat
print(f'A categoria com maior gasto foi "{catmaior}" com valor de {valmaior}\n')

# Nível 3
# Exercício 7
lista = session.query(Transacao, Categoria).join(Categoria).all()
for t, c in lista:
    print(f"{t.descricao} | {t.valor} | {c.categoria}")
print("")

# Exercício 8
mercado = (
    session.query(Transacao, Categoria)
    .join(Categoria)
    .filter(Categoria.categoria == "Mercado")
    .all()
)
print("Mercado")
for t, c in mercado:
    print(f"{t.descricao} -> {t.valor}")
print("")

# Exercício 9
todas = session.query(Transacao, Categoria).join(Categoria).all()
for t, c in todas:
    print(f"{t.descricao} | {t.valor} | {c.categoria} | {t.tipo}")
print("")

# Nível 4
# Exercício 10
total_cat = (
    session.query(Categoria.categoria, func.sum(Transacao.valor))
    .filter(Transacao.tipo == "saida")
    .group_by(Categoria.categoria)
    .join(Transacao)
    .all()
)
for i in total_cat:
    print(f"{i[0]} | {i[1]}")
print("")

# Exercício 11
total_cat = (
    session.query(Categoria.categoria, func.sum(Transacao.valor))
    .filter(Transacao.tipo == "entrada")
    .join(Transacao)
    .group_by(Categoria.categoria)
    .all()
)
for i in total_cat:
    print(f"{i[0]} | {i[1]}")
print("")

# Exercício 12
categorias = (
    session.query(Categoria.categoria, func.sum(Transacao.valor))
    .join(Transacao)
    .group_by(Categoria.categoria)
    .all()
)
for i in categorias:
    print(f"{i[0]} | {i[1]}")
print("")
