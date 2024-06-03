import sqlite3
con = sqlite3.connect('venv/senac/base_DeDados.db')
cur = con.cursor() #conectando cursor

def db_select(valorDoCampo, campo):
    return """ 
    SELECT id, nome, sobrenome, cpf, tempoDeServico, remuneracao
    FROM funcionarios
    WHERE {}={} """.format(valorDoCampo, campo)

print("""
+-------------------------+
Escolha uma das opções:
      1 - id
      2 - nome
      3 - sobrenome
      4 - cpf
      5 - tempoDeServico
      6 - remuneracao
+-------------------------+
""")
campo = int(input())
if(campo==1):
    valorDoCampo = input("Id: ")
    cur.execute(db_select(valorDoCampo, 'id'))
elif(campo==2):
    valorDoCampo = input("Nome: ")
    cur.execute(db_select(valorDoCampo, 'nome'))
elif(campo==3):
    valorDoCampo = input("Sobrenome: ")
    cur.execute(db_select(valorDoCampo, 'sobrenome'))
elif(campo==4):
    valorDoCampo = input("CPF: ")
    cur.execute(db_select(valorDoCampo, 'cpf'))
elif(campo==5):
    valorDoCampo = input("Tempo de Serviço: ")
    cur.execute(db_select(valorDoCampo, 'tempoDeServico'))
elif(campo==6):
    valorDoCampo = input("Remuneração: ")
    cur.execute(db_select(valorDoCampo, 'remuneracao'))

dados = cur.fetchone()
print(dados)
con.close()
