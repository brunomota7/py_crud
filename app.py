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

def listar_usuarios():
    conexao = sql.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM usuarios''')
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)
    conexao.close()

def atualizar_usuario(id, nome, email, senha):
    conexao = sql.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?''', (nome, email, senha, id))
    conexao.commit()
    conexao.close()

def deletar_usuario(id):
    conexao = sql.connect('usuarios.db')
    cursor = conexao.cursor()
    cursor.execute('''DELETE FROM usuarios WHERE id = ?''', (id))
    conexao.commit()
    conexao.close()