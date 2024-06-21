
from senacBank_servidor import db_updateCPF, db_updateTitular, db_updateSenha, db_updateSaldoC, db_updateSaldoP, db_delete, db_select, home
from pprint import pprint

def main():
    cliente, conta = home() #instancia
    while True:
        print("\nEscolha uma opção abaixo:           ")
        print("+====================================+")
        print("|   ****Gestão de Funcionários****   |")
        print("|          MENU DE OPÇÕES            |")
        print("|        1 - Buscar                  |")
        print("|        2 - Atualizar Dados         |")
        print("|        3 - Deletar                 |")
        print("|        4 - Home                    |")
        print("|        0 - Sair                    |")
        print("+====================================+")

        op = int(input())

        if(op==1):

            #BUSCAR

            print("""
            +-------------------------+
            | ****Buscar usuário****  |
            +-------------------------+
            |Buscar por:              |
            |   1 - Número da conta   |
            |   2 - Titular da conta  |
            |   3 - cpf               |
            +-------------------------+
            """)

            campo = int(input())

            if(campo==1):
                valorDoCampo = int(input("Número da Conta: "))
                pprint(db_select(valorDoCampo, 'conta'))
            if(campo==2):
                valorDoCampo = int(input("titular: "))
                pprint(db_select(valorDoCampo, 'titular'))
            elif(campo==3):
                valorDoCampo = input("CPF: ")
                pprint(db_select(valorDoCampo, 'cpf'))
            else:
                print("Erro: Selecione uma opção válida!")

        elif(op==2):

            #ATUALIZAR

            print("""
            +-------------------------+
            ****Alterar cadastro****
            +-------------------------+
            """)
            #conta = int(input("Digite o número da conta:\n"))

            print("""
            +-------------------------+
            Qual campo será alterado?\n
                1 - titular
                2 - cpf
                3 - senha
                4 - saldoC
                5 - saldoP
            +-------------------------+
            """)
            campo = int(input())

            if(campo==1):
                titular = input("novo titular: ")
                db_updateTitular(titular, conta)
            elif(campo==2):
                cpfNovo = input("novo cpf: ")
                conta = int(input("Qual o número da conta do cliente?\n"))
                db_updateCPF(cpfNovo, conta)
            elif(campo==3):
                senha = input("nova senha: ")
                db_updateSenha(senha, conta)
            elif(campo==4):
                print("""
                    +-------------------------+
                    Escolha uma das operações?\n
                        1 - sacar
                        2 - depositar
                        3 - aplicar
                    +-------------------------+
                    """)
                op = int(input())
                if(op==1):
                    senha = int(input("senha: "))
                    valor = float(input("Valor do saque: R$ "))
                    saldoC = cliente.sacar(valor)
                    #saldoC = input("novo saldoC: ")
                    db_updateSaldoC(saldoC, senha)
                if(op==2):
                    valor = float(input("Valor do depósito: R$ "))
                    saldoC = cliente.depositar(valor)
                    #saldoC = input("novo saldoC: ")
                    db_updateSaldoC(saldoC, conta)
            elif(campo==5):
                saldoP = input("novo saldoP: ")
                db_updateSaldoP(saldoP, conta)

            print("Atualização executada com sucesso!")

        elif(op==3):

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

        elif(op==4):
            cliente, conta = home() #instancia
    
        elif(op==0):
            print("Operação finalizada pelo usuário!\nObrigada por utilizar o Senac Bank 😊")
            #para exibir tela de emojis pressione:
            #windows(tecla com bandeira do windows) + . (tecla ponto)
            break

if __name__ == "__main__":
    main()


