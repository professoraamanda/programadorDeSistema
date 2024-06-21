from website import tabelaDeUsuarios, engine
conn = engine.connect() #conexão com banco de dados

#ins = tabelaDeUsuarios.insert()
#new_user = ins.values(nome='Fabio', idade=29, senha='rio')
#conn.execute(new_user)

conn.execute(tabelaDeUsuarios.insert(),[
    {'nome': 'Sara', 'idade': 21, 'senha': 'gatinha_123'},
    {'nome': 'Lívia', 'idade': 19, 'senha': 'Fuctur@54'},
    {'nome': 'Thaina', 'idade': 23, 'senha': 'Souz@L@0'},
    {'nome': 'Victor', 'idade': 19, 'senha': 'moNitor'},
    {'nome': 'Alex', 'idade': 25, 'senha': 'n@otouAqui'},
    {'nome': 'Guilherme', 'idade': 26, 'senha': 'J@eoFim'},
    {'nome': 'Sheeza', 'idade': 25, 'senha': 'onDeTou'}
])
