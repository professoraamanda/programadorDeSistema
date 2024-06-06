
from servidor import db_insert, db_select, db_updateCPF, db_updateNome
from servidor import db_updateRemuneracao, db_updateSobrenome, db_updateTS, db_delete
from pprint import pprint

def main():

    while True:
        print("\nEscolha uma opção abaixo:           ")
        print("+====================================+")
        print("|   ****Gestão de Funcionários****   |")
        print("|          MENU DE OPÇÕES            |")
        print("|        1 - Cadastrar               |")
        print("|        2 - Buscar                  |")
        print("|        3 - Atualizar Dados         |")
        print("|        4 - Deletar                 |")
        print("|        0 - Sair                    |")
        print("+====================================+")

        op = int(input())

        if(op==1):
            #CADASTRAR

            nome = input("nome: ")
            sobrenome = input("sobrenome: ")
            cpf = input("cpf: ")
            tempoDeServico = int(input("Tempo de serviço: "))
            remuneracao = int(input("Remuneração: "))

            db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao)
        
        elif(op==2):

            #BUSCAR

            print("""
            +-------------------------+
            | ****Buscar usuário****  |
            +-------------------------+
            |Buscar por:              |
            |      1 - id             |
            |      2 - nome           |
            |      3 - sobrenome      |
            |      4 - cpf            |
            |      5 - tempoDeServico |
            |      6 - remuneracao    |
            +-------------------------+
            """)

            campo = int(input())

            if(campo==1):
                valorDoCampo = int(input("Id: "))
                pprint(db_select(valorDoCampo, 'id'))
            elif(campo==2):
                valorDoCampo = input("Nome: ")
                pprint(db_select(valorDoCampo, 'nome'))
            elif(campo==3):
                valorDoCampo = input("Sobrenome: ")
                pprint(db_select(valorDoCampo, 'sobrenome'))
            elif(campo==4):
                valorDoCampo = int(input("CPF: "))
                pprint(db_select(valorDoCampo, 'cpf'))
            elif(campo==5):
                valorDoCampo = int(input("Tempo de Serviço: "))
                pprint(db_select(valorDoCampo, 'tempoDeServico'))
            elif(campo==6):
                valorDoCampo = int(input("Remuneração: "))
                pprint(db_select(valorDoCampo, 'remuneracao'))

        elif(op==3):

            #ATUALIZAR

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

        elif(op==4):

            #DELETAR

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
        
        elif(op==0):
            print("Operação finalizada pelo usuário!")
            break
            
        print("teste, ")

if __name__ == "__main__":
    main()


