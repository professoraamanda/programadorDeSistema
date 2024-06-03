import sqlite3
con = sqlite3.connect('venv/senac/base_DeDados.db')
cur = con.cursor() #conectando cursor



#cur.execute(db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao))
#cur.execute(db_update(nome, cpf))
con.commit() #executar os comandos na nossa base]
con.close()