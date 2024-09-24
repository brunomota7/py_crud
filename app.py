import sqlite3 as sql

def criar_tabela():
    conexao = sql.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    senha TEXT NOT NULL)''')
    conexao.commit()
    conexao.close()

def adicionar_usuario(nome, email, senha):
    conexao = sql.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)''', (nome, email, senha))
    conexao.commit()
    conexao.close()