from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///./v2_sqlalchemy/meubanco.db", echo=False)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

Base = declarative_base()
