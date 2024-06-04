from crud import db_select

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
    print(db_select(valorDoCampo, 'id'))
elif(campo==2):
    valorDoCampo = input("Nome: ")
    print(db_select(valorDoCampo, 'nome'))
elif(campo==3):
    valorDoCampo = input("Sobrenome: ")
    print(db_select(valorDoCampo, 'sobrenome'))
elif(campo==4):
    valorDoCampo = input("CPF: ")
    print(db_select(valorDoCampo, 'cpf'))
elif(campo==5):
    valorDoCampo = input("Tempo de Serviço: ")
    print(db_select(valorDoCampo, 'tempoDeServico'))
elif(campo==6):
    valorDoCampo = input("Remuneração: ")
    print(db_select(valorDoCampo, 'remuneracao'))
