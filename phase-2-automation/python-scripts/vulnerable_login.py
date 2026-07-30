#!/usr/bin/env python3
# =========================================================
# Script: vulnerable_login.py
# Descricao: Servidor Web com Formulario de Login para testes de SQLi
# Autor: Hiago (Purple Team Journey)
# =========================================================

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

class LoginHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Exibe a tela de login em HTML
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Portal Corporativo - Login</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #1e1e2e; color: #cdd6f4; text-align: center; padding-top: 50px; }
                .card { background-color: #313244; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
                input { margin: 10px; padding: 10px; width: 80%; border-radius: 5px; border: none; }
                button { padding: 10px 20px; background-color: #89b4fa; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🔐 Portal Restrito</h2>
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
        # Processa o envio dos dados do formulario
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        fields = urllib.parse.parse_qs(post_data)

        username = fields.get('username', [''])[0]
        password = fields.get('password', [''])[0]

        # Log do recebimento para auditoria Blue Team
        print(f"[LOG] Tentativa de login recebida - Usuario: {username} | Senha: {password}")

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # Simulacao de validacao simples
        if username == "admin" and password == "SuperSenha2026":
            response = "<h1>✅ Acesso Concedido! Bem-vindo Admin.</h1>"
        else:
            response = "<h1>❌ Acesso Negado! Credenciais incorretas.</h1>"

        self.wfile.write(response.encode('utf-8'))

def run_server():
    server_address = ('127.0.0.1', 8099)
    httpd = HTTPServer(server_address, LoginHandler)
    print("=" * 60)
    print("🚀 SERVIDOR DE LOGIN ATIVO EM http://127.0.0.1:8099")
    print("Abra o navegador no endereco acima para visualizar a interface.")
    print("=" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Servidor encerrado.")

if __name__ == "__main__":
    run_server()
