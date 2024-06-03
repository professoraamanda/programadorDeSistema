from crud import db_updateNome, db_updateRemuneracao, db_updateCPF, db_updateSobrenome, db_updateTS

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
    db_updateNome(nome, cpfE)
elif(campo==2):
    sobrenome = input("novo sobrenome: ")
    db_updateSobrenome(sobrenome, cpfE)
elif(campo==3):
    cpfNovo = input("novo cpf: ")
    id = int(input("Qual o id do usuário?\n"))
    db_updateCPF(cpfNovo, id)
elif(campo==4):
    tempoDeServico = input("novo tempo de serviço: ")
    db_updateTS(tempoDeServico, cpfE)
elif(campo==5):
    remuneracao = input("nova remuneração: ")
    db_updateRemuneracao(remuneracao, cpfE)

print("Atualização executada com sucesso!")
