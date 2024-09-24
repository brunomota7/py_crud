<h1 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">📋 Sistema de Gerenciamento de Usuários com Python e SQLite 💻</h1>

<p align="center" style="font-family: Arial, sans-serif; max-width: 800px; margin: auto; font-size: 1.2em;">
    Este projeto é um sistema simples de gerenciamento de usuários, utilizando <strong>Python</strong> e <strong>SQLite</strong>. O banco de dados é criado localmente e permite realizar operações CRUD (Create, Read, Update, Delete) em um banco de dados de usuários. Desenvolvido para ser utilizado via linha de comando.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Finalizado-brightgreen" alt="Status do Projeto">
  <img src="https://img.shields.io/badge/Python-3.x-blue" alt="Python">
  <img src="https://img.shields.io/badge/SQLite-integrado-lightgrey" alt="SQLite">
</p>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">🚀 Funcionalidades</h2>

<ul style="font-family: Arial, sans-serif; font-size: 1.1em; max-width: 800px; margin: auto; list-style-type: none;">
    <li>💾 <strong>Adicionar Usuário:</strong> Insere um novo usuário no banco de dados.</li>
    <li>📋 <strong>Listar Usuários:</strong> Exibe todos os usuários cadastrados.</li>
    <li>✏️ <strong>Atualizar Usuário:</strong> Atualiza os dados de um usuário existente.</li>
    <li>❌ <strong>Deletar Usuário:</strong> Remove um usuário do banco de dados.</li>
</ul>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">📂 Estrutura do Projeto</h2>
<p style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
    O projeto contém as seguintes funções principais:
</p>

<h3 style="font-family: Arial, sans-serif;">1. criar_tabela()</h3>
<p style="font-family: Arial, sans-serif;">
    Cria a tabela <strong>usuarios</strong> no banco de dados <strong>usuarios.db</strong>, se ainda não existir.
</p>

<h4 style="font-family: Arial, sans-serif; color: #555;">Exemplo de SQL gerado:</h4>
<pre style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);
</pre>

<h3 style="font-family: Arial, sans-serif;">2. adicionar_usuario(nome, email, senha)</h3>
<p style="font-family: Arial, sans-serif;">
    Insere um novo usuário no banco de dados.
</p>
<pre style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?);
</pre>

<h3 style="font-family: Arial, sans-serif;">3. listar_usuarios()</h3>
<p style="font-family: Arial, sans-serif;">
    Exibe todos os usuários cadastrados na tabela <strong>usuarios</strong>.
</p>
<pre style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
SELECT * FROM usuarios;
</pre>

<h3 style="font-family: Arial, sans-serif;">4. atualizar_usuario(id, nome, email, senha)</h3>
<p style="font-family: Arial, sans-serif;">
    Atualiza os dados de um usuário com base no seu <strong>id</strong>.
</p>
<pre style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
UPDATE usuarios SET nome = ?, email = ?, senha = ? WHERE id = ?;
</pre>

<h3 style="font-family: Arial, sans-serif;">5. deletar_usuario(id)</h3>
<p style="font-family: Arial, sans-serif;">
    Remove um usuário da tabela <strong>usuarios</strong>.
</p>
<pre style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 10px; border-radius: 5px;">
DELETE FROM usuarios WHERE id = ?;
</pre>

<h3 style="font-family: Arial, sans-serif;">6. menu()</h3>
<p style="font-family: Arial, sans-serif;">
    Exibe o menu de opções disponíveis para o usuário.
</p>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">🛠️ Como Executar o Projeto</h2>
<ol style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
    <li>Clone o repositório para sua máquina local:</li>
    <pre style="font-family: Arial, sans-serif;">git clone https://github.com/seu-usuario/seu-repositorio.git</pre>
    <li>Navegue até o diretório do projeto:</li>
    <pre style="font-family: Arial, sans-serif;">cd seu-repositorio</pre>
    <li>Execute o script Python:</li>
    <pre style="font-family: Arial, sans-serif;">python nome_do_arquivo.py</pre>
    <li>Use o menu para navegar pelas opções disponíveis.</li>
</ol>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">⚙️ Requisitos</h2>
<ul style="font-family: Arial, sans-serif; max-width: 800px; margin: auto;">
    <li>Python 3.x instalado.</li>
    <li>SQLite3 (gerenciado automaticamente pelo Python via sqlite3).</li>
</ul>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">📌 Exemplo de Uso</h2>

<h4 style="font-family: Arial, sans-serif;">Adicionar Usuário:</h4>
<pre style="font-family: Arial, sans-serif;">
Escolha uma opção: 1
Digite o nome do usuário: João Silva
Digite o email: joao@exemplo.com
Digite a senha: senha123
Usuário adicionado com sucesso!</pre>

<h4 style="font-family: Arial, sans-serif;">Listar Usuários:</h4>
<pre style="font-family: Arial, sans-serif;">
Escolha uma opção: 2
Todos os usuários:
(1, 'João Silva', 'joao@exemplo.com', 'senha123')</pre>

<h4 style="font-family: Arial, sans-serif;">Atualizar Usuário:</h4>
<pre style="font-family: Arial, sans-serif;">
Escolha uma opção: 3
Digite o ID do usuário a ser atualizado: 1
Digite o novo nome do usuário: João S. Silva
Digite o novo email: joao.silva@exemplo.com
Digite a nova senha: nova_senha123
Usuário atualizado com sucesso!</pre>

<h4 style="font-family: Arial, sans-serif;">Deletar Usuário:</h4>
<pre style="font-family: Arial, sans-serif;">
Escolha uma opção: 4
Digite o ID do usuário a ser deletado: 1
Usuário deletado com sucesso!</pre>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">🧑‍💻 Contribuidores</h2>
<p align="center" style="font-family: Arial, sans-serif;">
    Feito por <strong>Bruno Mota</strong>. 
    Quer contribuir? Sinta-se à vontade para enviar pull requests ou sugerir melhorias!
</p>

---

<h2 align="center" style="font-family: Arial, sans-serif; color: #4A90E2;">🔗 Vamos nos conectar?</h2>
<p align="center">
  <a href="https://www.linkedin.com/in/bruno-mota-dev/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
</p>

---

<p align="center" style="font-family: Arial, sans-serif;">✨ Desfrute e aprenda enquanto usa este sistema simples! ✨</p>
