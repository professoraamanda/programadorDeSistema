import sqlite3
con = sqlite3.connect('venv/senac/base_DeDados.db')
cur = con.cursor() #conectando cursor

def db_delete(cpf):
    return """
    DELETE FROM funcionarios 
    WHERE cpf = '{}'  """.format(cpf)

print("""
+-------------------------+
 ****Deletar cadastro****
+-------------------------+
""")
cpf = int(input("informe o CPF:\n"))

print("""
+-------------------------------------+
 ****Tem certeza que deseja deletar****
                1 - sim
                0 - não
+-------------------------------------+
""")
op = int(input())
if(op==1):
    cur.execute(db_delete(cpf))
    print("usuário excluído com sucesso!")
    con.commit() #executar os comandos na nossa base
    con.close()
