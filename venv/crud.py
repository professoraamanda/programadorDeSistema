import sqlite3

def commit_close(funcao):
    def decorator(*argumentos):
        con = sqlite3.connect('base_DeDados.db')
        cur = con.cursor() #conectando cursor
        sql = funcao(*argumentos)
        cur.execute(sql)
        con.commit()
        con.close()
        print("ok!")
    return decorator

@commit_close
def db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao):
    return """
    INSERT INTO funcionarios (nome, sobrenome, cpf, tempoDeServico, remuneracao)
        VALUES('{}','{}','{}', {}, {})
    """.format(nome, sobrenome, cpf, tempoDeServico, remuneracao)

@commit_close
def db_updateNome(nome, cpf):
    return """
    UPDATE funcionarios SET nome = '{}' 
    WHERE cpf = '{}'  """.format(nome, cpf)

@commit_close
def db_updateSobrenome(sobrenome, cpf):
    return """
    UPDATE funcionarios SET sobrenome = '{}' 
    WHERE cpf = '{}'  """.format(sobrenome, cpf)

@commit_close
def db_updateCPF(cpf, id):
    return """
    UPDATE funcionarios SET cpf = '{}' 
    WHERE id = '{}'  """.format(cpf, id)

@commit_close
def db_updateTS(tempoDeServico, cpf):
    return """
    UPDATE funcionarios SET tempoDeServico = '{}' 
    WHERE cpf = '{}'  """.format(tempoDeServico, cpf)

@commit_close
def db_updateRemuneracao(remuneracao, cpf):
    return """
    UPDATE funcionarios SET remuneracao = '{}' 
    WHERE cpf = '{}'  """.format(remuneracao, cpf)

@commit_close
def db_delete(cpf):
    return """
    DELETE FROM funcionarios 
    WHERE cpf = '{}'  """.format(cpf)

def db_select(valorDoCampo, campo):
    con = sqlite3.connect('base_DeDados.db')
    cur = con.cursor()  # conectando cursor
    sql = """ 
    SELECT id, nome, sobrenome, cpf, tempoDeServico, remuneracao
    FROM funcionarios
    WHERE {}=? 
    """.format(valorDoCampo)
    print("SQL:", sql)
    cur.execute(sql, (campo,))
    data = cur.fetchall()
    con.close()
    return data


