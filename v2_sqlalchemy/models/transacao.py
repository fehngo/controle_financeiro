from sqlalchemy import Column, Float, ForeignKey, Integer, String

from v2_sqlalchemy.database.connection import Base


class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    tipo = Column(String, nullable=False)
    data = Column(String)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    def __repr__(self):
        return f"<Transacao(descricao={self.descricao}, valor={self.valor})>"
