
from crud import db_insert

nome = input("nome: ")
sobrenome = input("sobrenome: ")
cpf = input("cpf: ")
tempoDeServico = int(input("Tempo de serviço: "))
remuneracao = int(input("Remuneração: "))

db_insert(nome, sobrenome, cpf, tempoDeServico, remuneracao)

db_insert('Amanda', 'Xavier', 589647889, 5, 5000)
db_insert('Victor', 'Augusto', 1456987428, 2, 6000)
db_insert('Renata', 'Maria', 1478569433, 3, 3600)
db_insert('Sheeza', 'Mendes', 1452636698, 7, 12000)
db_insert('Sara', 'Oliveira', 147584669, 4, 9000)
db_insert('Thaina', 'Silva', 123654879, 6, 4000)
db_insert('Alex', 'Jorge', 569874563, 1, 1500)
db_insert('Livia', 'Andrade', 569845321, 2, 8000)

