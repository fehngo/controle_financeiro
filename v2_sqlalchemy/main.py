from v2_sqlalchemy.database.connection import Base, engine, session
from v2_sqlalchemy.models.categoria import Categoria  # noqa
from v2_sqlalchemy.models.transacao import Transacao  # noqa

Base.metadata.create_all(bind=engine)

Cat = [
    Categoria(categoria="Salario"),
    Categoria(categoria="Mercado"),
    Categoria(categoria="Combustivel"),
    Categoria(categoria="Farmacia"),
    Categoria(categoria="Lazer"),
    Categoria(categoria="FastFood"),
    Categoria(categoria="Outros"),
]
session.add_all(Cat)
session.commit()

# categoria_salario = session.query(Categoria).filter_by(categoria="Salario").first()
# categoria_mercado = session.query(Categoria).filter_by(categoria="Mercado").first()
# categoria_combustivel = session.query(Categoria).filter_by(categoria="Combustivel").first()
# categoria_farmacia = session.query(Categoria).filter_by(categoria="Farmacia").first()
# categoria_lazer = session.query(Categoria).filter_by(categoria="Lazer").first()
# categoria_fastfood = session.query(Categoria).filter_by(categoria="FastFood").first()
# categoria_outros = session.query(Categoria).filter_by(categoria="Outros").first()
categorias = session.query(Categoria).all()
print(categorias)
categoria_id = {}
for c in categorias:
    categoria_id[c.categoria] = c.id
# print(categoria_id)

trans = [
    Transacao(
        descricao="Pagamento Janeiro",
        valor=3500.00,
        tipo="entrada",
        data="01-01-2026",
        categoria_id=categoria_id["Salario"],
    ),
    Transacao(
        descricao="Combustivel ida trabalho",
        valor=50.00,
        tipo="saida",
        data="02-01-2026",
        categoria_id=categoria_id["Combustivel"],
    ),
    Transacao(
        descricao="Jantar Romantico",
        valor=127.78,
        tipo="saida",
        data="02-01-2026",
        categoria_id=categoria_id["Mercado"],
    ),
    Transacao(
        descricao="Posto nota 10",
        valor=50.00,
        tipo="saida",
        data="05-01-2026",
        categoria_id=categoria_id["Combustivel"],
    ),
    Transacao(
        descricao="Remedio Filho",
        valor=67.41,
        tipo="saida",
        data="07-01-2026",
        categoria_id=categoria_id["Farmacia"],
    ),
    Transacao(
        descricao="Posto nota 10",
        valor=50.00,
        tipo="saida",
        data="07-01-2026",
        categoria_id=categoria_id["Combustivel"],
    ),
    Transacao(
        descricao="Macarrao Molho Branco",
        valor=47.29,
        tipo="saida",
        data="10-01-2026",
        categoria_id=categoria_id["Mercado"],
    ),
    Transacao(
        descricao="Posto nota 10",
        valor=50.00,
        tipo="saida",
        data="11-01-2026",
        categoria_id=categoria_id["Combustivel"],
    ),
    Transacao(
        descricao="Acai Parque",
        valor=17.00,
        tipo="saida",
        data="11-01-2026",
        categoria_id=categoria_id["Lazer"],
    ),
    Transacao(
        descricao="Pizza noite",
        valor=54.74,
        tipo="saida",
        data="11-01-2026",
        categoria_id=categoria_id["FastFood"],
    ),
    Transacao(
        descricao="Jogo Videogame",
        valor=274.78,
        tipo="saida",
        data="12-01-2026",
        categoria_id=categoria_id["Outros"],
    ),
]
session.add_all(trans)
session.commit()
