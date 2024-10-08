import sqlite3
def obter_conecxao():
    "retornar uma conecxao com banco de dados SQLite chamado 'dados.db.'"
    conecxao = SQLite3.connect('dados db') # type: ignore
    return conecxao 

conecxao = obter_conecxao()
cursor = conecxao.cursor()
