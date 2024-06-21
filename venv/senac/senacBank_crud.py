
from senacBank_servidor import db_updateCPF, db_updateTitular, db_updateSenha, db_updateSaldoC, db_updateSaldoP
from senacBank_servidor import db_delete, db_select, home
from pprint import pprint

def main():
    cliente, conta = home() #instancia
    while True:
        print("""\nEscolha uma opção abaixo:           
               +====================================+
               |        ****Senac Bank****          |
               |          MENU DE OPÇÕES            |
               |        1 - Sacar                   |
               |        2 - Aplicar                 |
               |        3 - Resgatar                |
               |        4 - Mostrar Dados           |
               |        5 - Atualizar Dados         |
               |        6 - Home                    |
               |        0 - Sair                    |
               +====================================+""")

        op = int(input())

        if(op==1): #sacar
            valor = float(input("Valor do saque: R$ "))
            saldoC = cliente.sacar(valor)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, conta)

        elif(op==2): #aplicar
            valor = float(input("Valor para aplicação: R$ "))
            saldoC, saldoP = cliente.aplicar(valor, cliente)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, conta)
            db_updateSaldoP(saldoP, conta)

        elif(op==3): #resgatar
            valor = float(input("Valor para resgate: R$ "))
            saldoC, saldoP = cliente.resgatar(valor, cliente)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, conta)
            db_updateSaldoP(saldoP, conta)

        elif(op==4): #mostrar dados
            cliente.mostrarDados()

        elif(op==5):

            #ATUALIZAR

            print("""
            +-------------------------+
            |  ****Alterar Dados****  |
            +-------------------------+
            |Qual campo será alterado?|
            |    1 - Buscar usuário   |
            |    2 - Excluir usuário  |
            |    3 - Alterar nome     |
            |    4 - Alterar cpf      |
            |    5 - Alterar senha    |
            |    _ - saldoP           |
            |    0 - Menu anterior    |
            +-------------------------+
            """)

            campo = int(input())

            if(campo==1):

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

                opcao = int(input())

                if(opcao==1):
                    valorDoCampo = int(input("Número da Conta: "))
                    pprint(db_select(valorDoCampo, 'conta'))
                elif(opcao==2):
                    valorDoCampo = int(input("titular: "))
                    pprint(db_select(valorDoCampo, 'titular'))
                elif(opcao==3):
                    valorDoCampo = input("CPF: ")
                    pprint(db_select(valorDoCampo, 'cpf'))
                else:
                    print("Erro: Selecione uma opção válida!")
            
            elif(campo == 2):

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

            elif(campo==3): #titular
                titular = input("novo titular: ")
                db_updateTitular(titular, conta)
            elif(campo==4): #cpf
                cpfNovo = input("novo cpf: ")
                conta = int(input("Qual o número da conta do cliente?\n"))
                db_updateCPF(cpfNovo, conta)
            elif(campo==5): #senha
                senha = input("nova senha: ")
                db_updateSenha(senha, conta)
            elif(campo==7): #saldoP
                saldoP = input("novo saldoP: ")
                db_updateSaldoP(saldoP, conta)
            
            elif(campo == 0):
                pass

            print("Atualização executada com sucesso!")

        elif(op==6):
            cliente, conta = home() #instancia
    
        elif(op==0):
            print("Operação finalizada pelo usuário!\nObrigada por utilizar o Senac Bank 😊")
            home()
            #para exibir tela de emojis pressione:
            #windows(tecla com bandeira do windows) + . (tecla ponto)
            break

if __name__ == "__main__":
    main()


