#!/usr/bin/env python3
# =========================================================
# Script: vulnerable_login.py
# Descricao: Servidor Web com Banco SQLite vulneravel a SQL Injection
# Autor: Hiago (Purple Team Journey)
# =========================================================

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import sqlite3

# Inicializa um banco de dados SQLite em memoria para testes
def init_db():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    # Cria tabela de usuarios
    cursor.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    ''')
    # Insere o usuario administrador no banco
    cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'SuperSenha2026')")
    conn.commit()
    return conn

# Instancia o banco de dados global do lab
DB_CONN = init_db()

class LoginHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Lab Purple Team - Login Vulneravel (SQLi)</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #1e1e2e; color: #cdd6f4; text-align: center; padding-top: 50px; }
                .card { background-color: #313244; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
                input { margin: 10px; padding: 10px; width: 80%; border-radius: 5px; border: none; }
                button { padding: 10px 20px; background-color: #89b4fa; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🔐 Portal Restrito (Lab SQLi)</h2>
                <form action="/login" method="POST">
                    <input type="text" name="username" placeholder="Usuario" required><br>
                    <input type="password" name="password" placeholder="Senha" required><br>
                    <button type="submit">Entrar</button>
                </form>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        fields = urllib.parse.parse_qs(post_data)

        username = fields.get('username', [''])[0]
        password = fields.get('password', [''])[0]

        # 🚨 VULNERABILIDADE AQUI: Concatenação direta de strings na Query SQL!
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        print("=" * 60)
        print(f"📥 Dados Recebidos -> Usr: {username} | Pwd: {password}")
        print(f"🔍 QUERY EXECUTADA NO BANCO:\n   {query}")
        print("=" * 60)

        cursor = DB_CONN.cursor()
        
        try:
            cursor.execute(query)
            user = cursor.fetchone()

            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            if user:
                response = f"<h1>✅ ACESSO CONCEDIDO! Bem-vindo, {user[1]} (FLAG{{SQLI_BYPASS_SUCCESS}})</h1>"
            else:
                response = "<h1>❌ ACESSO NEGADO! Credenciais invalidas.</h1>"

        except sqlite3.OperationalError as e:
            self.send_response(500)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            response = f"<h1>⚠️ ERRO DE SINTAXE SQL: {e}</h1>"

        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('127.0.0.1', 8099)
    httpd = HTTPServer(server_address, LoginHandler)
    print("=" * 60)
    print("🚀 SERVIDOR DE TESTES SQLi RODANDO EM http://127.0.0.1:8099")
    print("Pressione Ctrl + C para encerrar.")
    print("=" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Servidor encerrado.")

if __name__ == "__main__":
    run_server()
