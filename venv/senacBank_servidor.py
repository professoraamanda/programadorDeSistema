import sqlite3

def commit_close(funcao):
    def decorator(*argumentos):
        con = sqlite3.connect('venv/senac/dataset_banco.db')
        cur = con.cursor() #conectando cursor
        sql = funcao(*argumentos)
        cur.execute(sql)
        con.commit()
        con.close()
        print("ok!")
    return decorator

@commit_close
def db_insert(titular, cpf, senha, saldoC, saldoP):
    return """
    INSERT INTO dataset_clientes (titular, cpf, senha, saldoC, saldoP)
        VALUES('{}',{},{}, {}, {})
    """.format(titular, cpf, senha, saldoC, saldoP)

@commit_close
def db_updateTitular(titular, conta):
    return """
    UPDATE dataset_clientes SET titular = '{}' 
    WHERE conta = {}  """.format(titular, conta)

@commit_close
def db_updateCPF(cpf, conta):
    return """
    UPDATE dataset_clientes SET cpf = {} 
    WHERE conta = '{}'  """.format(cpf, conta)

@commit_close
def db_updateSenha(senha, conta):
    return """
    UPDATE dataset_clientes SET senha = {} 
    WHERE conta = {}  """.format(senha, conta)

@commit_close
def db_updateSaldoC(saldoC, senha):
    return """
    UPDATE dataset_clientes SET saldoC = {}
    WHERE senha = {}  """.format(saldoC, senha)

@commit_close
def db_updateSaldoP(saldoP, senha):
    return """
    UPDATE dataset_clientes SET saldoP = {}
    WHERE senha = {}  """.format(saldoP, senha)

@commit_close
def db_delete(cpf):
    return """
    DELETE FROM dataset_clientes 
    WHERE cpf = {}  """.format(cpf)

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

def home():
     while True:
        op = int(input(("""\nSeja bem-vindo ao Senac Bank   
                +====================================+
                |      1 - Já sou cliente            |
                |      2 - Abrir conta               |
                |      0 - Encerrar                  |          
                +====================================+\n""")))
        if(op==0):
            break
        elif(op==2):
            #CADASTRAR

            titular = input("Titular: ")
            cpf = input("cpf: ")
            senha = int(input("senha (numérica de 4 dígitos): "))
            saldoC = 0
            saldoP = 0

            cliente = ContaCorrente(titular, cpf, senha, saldoC) #instancia
        
            print("Deve ser feito um depósito inicial para abertura de conta!")
            valor = float(input("Valor do depósito: R$ "))
            saldoC = cliente.depositar(valor)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, cpf)

            db_insert(titular, cpf, senha, saldoC, saldoP)
        elif(op==1):
            print("""\nEntre com seus dados""")
            valorDoCampo = int(input("Número da Conta: "))
            conta, titular, cpf, saldoC, saldoP = (db_select(valorDoCampo, 'conta'))
            print(conta, titular, cpf, saldoC, saldoP)
            senha = int(input("senha: "))            
            cliente = ContaCorrente(titular, cpf, senha, saldoC) #instancia
        return cliente, conta
     

class ContaCorrente():
    def __init__(self, titular, cpf, senha, saldoC=0):
        self.titular = titular
        self.cpf = cpf
        self.senha = senha
        self.saldoC = saldoC

    def sacar(self, valorDoSaque):
            if valorDoSaque <= self.saldoC:
                self.saldoC -= valorDoSaque
                print(f"Saque de R${valorDoSaque:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente.")
            return self.saldoC

    def depositar(self, valorDoDeposito):
            self.saldoC += valorDoDeposito
            print(f"Depósito de R${valorDoDeposito:.2f} realizado com sucesso.")
            return self.saldoC

    

    


