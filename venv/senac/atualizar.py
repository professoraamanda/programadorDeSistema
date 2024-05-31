import sqlite3
con = sqlite3.connect('venv/senac/base_DeDados.db')
cur = con.cursor() #conectando cursor

def db_updateNome(nome, cpf):
    return """
    UPDATE funcionarios SET nome = '{}' 
    WHERE cpf = '{}'  """.format(nome, cpf)

def db_updateSobrenome(sobrenome, cpf):
    return """
    UPDATE funcionarios SET sobrenome = '{}' 
    WHERE cpf = '{}'  """.format(sobrenome, cpf)

def db_updateCPF(cpf, id):
    return """
    UPDATE funcionarios SET cpf = '{}' 
    WHERE id = '{}'  """.format(cpf, id)

def db_updateTS(tempoDeServico, cpf):
    return """
    UPDATE funcionarios SET tempoDeServico = '{}' 
    WHERE cpf = '{}'  """.format(tempoDeServico, cpf)

def db_updateRemuneracao(remuneracao, cpf):
    return """
    UPDATE funcionarios SET remuneracao = '{}' 
    WHERE cpf = '{}'  """.format(remuneracao, cpf)

print("""
+-------------------------+
 ****Alterar cadastro****
+-------------------------+
""")
cpfE = int(input("Digite o CPF:\n"))

print("""
+-------------------------+
Qual campo será alterado?\n
      1 - nome
      2 - sobrenome
      3 - cpf
      4 - tempoDeServico
      5 - remuneracao
+-------------------------+
""")
campo = int(input())
if(campo==1):
    nome = input("novo nome: ")
    cur.execute(db_updateNome(nome, cpfE))
elif(campo==2):
    sobrenome = input("novo sobrenome: ")
    cur.execute(db_updateSobrenome(sobrenome, cpfE))
elif(campo==3):
    cpfNovo = input("novo cpf: ")
    id = int(input("Qual o id do usuário?\n"))
    cur.execute(db_updateCPF(cpfNovo, id))
elif(campo==4):
    tempoDeServico = input("novo tempo de serviço: ")
    cur.execute(db_updateTS(tempoDeServico, cpfE))
elif(campo==5):
    remuneracao = input("nova remuneração: ")
    cur.execute(db_updateRemuneracao(remuneracao, cpfE))

print("Atualização executada com sucesso!")

con.commit() #executar os comandos na nossa base]
con.close()