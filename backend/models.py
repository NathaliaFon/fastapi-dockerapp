from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base
from sqlalchemy.sql import func
#from sqlalchemy_utils import EmailType
#cria o a tabela tarefas



class Produtos(Base):
    __tablename__ = "produtos"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    item = Column('item', String, nullable=False)
    peso = Column('peso', Float)
    numero_caixas = Column('numero_caixas', Integer)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())


#arquivo 2
class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String, nullable=False, unique=True)
    password = Column('password', String, nullable=False)
    user_email = Column('user_email', String, nullable=True, unique=True)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, onupdate=func.now())
