import sqlite3
con = sqlite3.connect('venv/senac/dataset_banco.db') #criando base
cur = con.cursor() #conectando cursor
#sintaxe do sql
sql = """
CREATE TABLE dataset_clientes(conta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    titular TEXT NOT NULL,
                    cpf INTEGER NOT NULL,
                    senha INTEGER NOT NULL,
                    saldoC FLOAT NOT NULL,
                    saldoP FLOAT NOT NULL)
"""
cur.execute(sql)
con.commit() #executar os comandos na nossa base
con.close()