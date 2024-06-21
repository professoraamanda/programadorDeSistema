import sqlite3
from pprint import pprint

def db_select(valorDoCampo, campo):
        con = sqlite3.connect('venv/senac/dataset_banco.db')
        cur = con.cursor() #conectando cursor
        sql = """ 
        SELECT conta, titular, cpf, saldoC, saldoP
        FROM dataset_clientes
        WHERE {}='{}'
        """.format(campo, valorDoCampo)
        cur.execute(sql)
        dados = cur.fetchone()
        con.close()
        return dados

print("""\nEntre com seus dados""")
valorDoCampo = int(input("Número da Conta: "))
pprint((db_select(valorDoCampo, 'conta')))
conta, titular, cpf, saldoC, saldoP = (db_select(valorDoCampo, 'conta'))
print(conta, titular, cpf, saldoC, saldoP)