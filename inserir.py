import sqlite3
con = sqlite3.connect('venv/senac/base_DeDados.db')
cur = con.cursor() #conectando cursor

def db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao):
    return """
    INSERT INTO funcionarios (nome, sobrenome, cpf, tempoDeServico, remuneracao)
        VALUES('{}','{}','{}', {}, {})
    """.format(nome, sobrenome, cpf, tempoDeServico, remuneracao)

nome = input("nome: ")
sobrenome = input("sobrenome: ")
cpf = input("cpf: ")
tempoDeServico = int(input("Tempo de serviço: "))
remuneracao = int(input("Remuneração: "))

cur.execute(db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao))
con.commit() #executar os comandos na nossa base]
con.close()