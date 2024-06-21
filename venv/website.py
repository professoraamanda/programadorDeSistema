from datetime import datetime #trabalhar com datas e horas em python
#SQLAlchemy é uma biblioteca popular de mapeamento objeto-relacional(ORM) para Python, 
#que simplifica a interação com bancos de dados relacionais.
from sqlalchemy import (create_engine, MetaData, Column, Table,
                        Integer, String, DateTime) #importando várias classes e funções do SQLAlchemy

engine = create_engine('sqlite:///web.db', echo=True) #conexão com banco de dados
metadata = MetaData() #criando objeto metadata onde ficarão os dados 
tabelaDeUsuarios = Table('usuarios', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('nome', String(40), index = True),
                   Column('idade', Integer, nullable=False),
                   Column('senha', String),
                   Column('criado_em', DateTime, default=datetime.now),
                   Column('atualizado_em', DateTime, default=datetime.now,
                          onupdate=datetime.now))
metadata.create_all(engine) #criando todas as tabelas definidas e conectando os dados ao engine


