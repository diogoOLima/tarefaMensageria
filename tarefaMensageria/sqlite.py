import sqlite

banco = sqlite.connect('meubanco.sqlite')

cursor = banco.cursor()

cursor.execute("CREATE TABLE carrinho (id INTEGER NOT NULL, preco FLOAT NOT NULL, qtd INTEGER NOT NULL, produto_id INTEGER, venda_id INTEGER, PRIMARY KEY (id), FOREIGN KEY(produto_id) REFERENCES produto (id), FOREIGN KEY(venda_id) REFERENCES venda (id))")

cursor.execute("CREATE TABLE venda (id INTEGER NOT NULL, cliente_id INTEGER, cartao VARCHAR, pagamentoAprovado INTEGER, PRIMARY KEY (id), FOREIGN KEY(cliente_id) REFERENCES cliente (id))")

cursor.execute("CREATE TABLE produto (id INTEGER NOT NULL, nome VARCHAR NOT NULL, preco FLOAT NOT NULL, PRIMARY KEY (id))")

cursor.execute("CREATE TABLE cliente id INTEGER NOT NULL, nome VARCHAR NOT NULL, endereco VARCHAR NOT NULL, PRIMARY KEY (id))")

cursor.execute(" ")

cursor.execute(" ")
banco.commit()