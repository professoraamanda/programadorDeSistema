from crud import db_delete

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
    db_delete(cpf)
    print("usuário excluído com sucesso!")


