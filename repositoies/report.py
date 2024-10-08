from util import obter_conexao


class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade


def criar_tabela():
    conexao = obter_conexao()
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL,
            quantidade INTEGER NOT NULL
        )
    ''')
    
    conexao.commit()
    conexao.close()


def inserir(produto: Produto):
    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute('''
        INSERT INTO produtos (nome, descricao, preco, quantidade)
        VALUES (?, ?, ?, ?)
    ''', (produto.nome, produto.descricao, produto.preco, produto.quantidade))
    
    conexao.commit()
    conexao.close()


def obter_todos():
    conexao = obter_conexao()
    cursor = conexao.cursor()

    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    
    lista_produtos = []
    for produto in produtos:
        p = Produto(nome=produto[1], descricao=produto[2], preco=produto[3], quantidade=produto[4])
        lista_produtos.append(p)
    
    conexao.close()
    return lista_produtos
