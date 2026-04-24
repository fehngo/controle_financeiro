from sqlalchemy import Column, Integer, String

from v2_sqlalchemy.database.connection import Base


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column("id", Integer, autoincrement=True, primary_key=True)
    categoria = Column(String, nullable=False)

    def __repr__(self):
        return f"<Categoria(categoria={self.categoria})>"
