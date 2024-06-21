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
def db_updateSaldoC(saldoC, conta):
    return """
    UPDATE dataset_clientes SET saldoC = {}
    WHERE conta = {}  """.format(saldoC, conta)

@commit_close
def db_updateSaldoP(saldoP, conta):
    return """
    UPDATE dataset_clientes SET saldoP = {}
    WHERE conta = {}  """.format(saldoP, conta)

@commit_close
def db_delete(cpf):
    return """
    DELETE FROM dataset_clientes 
    WHERE cpf = {}  """.format(cpf)

def db_select(valorDoCampo, campo):
        con = sqlite3.connect('venv/senac/dataset_banco.db')
        cur = con.cursor() #conectando cursor
        sql = """ 
        SELECT conta, titular, cpf, senha, saldoC, saldoP
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
                |      3 - Fazer um depósito         |         
                +====================================+\n""")))
        
        if(op==2):
            #CADASTRAR

            titular = input("Titular: ")
            cpf = input("cpf: ")
            senha = int(input("senha (numérica de 4 dígitos): "))
            saldoC = 0
            saldoP = 0

            cliente = ContaPoupanca(titular, cpf, senha, saldoC, saldoP) #instancia
        
            print("Deve ser feito um depósito inicial para abertura de conta!")
            valor = float(input("Valor do depósito: R$ "))
            saldoC = cliente.depositar(valor)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, cpf)
            db_insert(titular, cpf, senha, saldoC, saldoP) #cria uma conta
            print("Conta criada com sucesso!")

            conta, titular, cpf, senha, saldoC, saldoP = (db_select(cpf, 'cpf'))

        elif(op==1): #consultar
            print("""\nEntre com seus dados""")
            valorDoCampo = int(input("Número da Conta: "))
            conta, titular, cpf, senha, saldoC, saldoP = (db_select(valorDoCampo, 'conta'))
            print(conta, titular, cpf, saldoC, saldoP)
            senha = int(input("senha: "))            
            cliente = ContaPoupanca(titular, cpf, senha, saldoC, saldoP) #instancia

        elif(op==3): #depositar
            conta = int(input("conta: "))
            conta, titular, cpf, senha, saldoC, saldoP = (db_select(conta, 'conta'))
            cliente = ContaPoupanca(titular, cpf, senha, saldoC, saldoP) #instancia
            valor = float(input("Valor do depósito: R$ "))
            saldoC = cliente.depositar(valor)
            #saldoC = input("novo saldoC: ")
            db_updateSaldoC(saldoC, conta)

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
    
    def aplicar(self, valorDaAplicacao, ContaPoupanca):
      if valorDaAplicacao <= self.saldoC:
        self.saldoC -= valorDaAplicacao #variavel para aplicação
        ContaPoupanca.depositoP(valorDaAplicacao) #deposita na conta poupança
        print(f"Aplicação na Poupança de R${valorDaAplicacao:.2f} realizado com sucesso.")
      else:
        print("Saldo insuficiente.")

      return self.saldoC, self.saldoP

class ContaPoupanca(ContaCorrente):
    def __init__(self, titular, cpf, senha, saldoC=0, saldoP=0):
        super().__init__(titular, cpf, senha, saldoC)
        self.saldoP = saldoP
    
    def depositoP(self, valorDoDeposito):
      self.saldoP += valorDoDeposito
      print(f"Depósito de R${valorDoDeposito:.2f} realizado com sucesso.")
      return self.saldoP

    def resgatar(self, valorDoResgate, ContaCorrente):
      if valorDoResgate <= self.saldoP:
        self.saldoP -= valorDoResgate #subtrai do saldo da poupança
        ContaCorrente.depositar(valorDoResgate) #deposita na conta corrente
        print(f"Resgate de R${valorDoResgate:.2f} para Conta Corrente realizado com sucesso.")
      else:
        print("Saldo insuficiente.")

      return self.saldoC, self.saldoP

    def mostrarDados(self):
        conta, titular, cpf, senha, saldoC, saldoP = (db_select(self.senha, 'senha'))
        print("""
        +------------------------------------------------+
        | Titular Conta Corrente: {}
        | Número da conta: {}
        | Saldo Conta Corrente: R$ {}
        | Saldo Conta Poupança: R$ {}
        +------------------------------------------------+
      """.format(titular, conta, saldoC, saldoP))

      

    

    


