#!/usr/bin/env python3
# =========================================================
# Script: web_server.py
# Descricao: Servidor Web HTTP simples para testes de laboratorio
# Autor: Hiago (Purple Team Journey)
# =========================================================

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Se o usuario tentar acessar a rota secreta:
        if self.path == "/secret-admin":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>PAINEL ADMIN RESTRITO - FLAG{{PURPLE_TEAM_2026}}</h1>")
        else:
            # Rota padrao (404 para qualquer outra coisa)
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>404 - Pagina Nao Encontrada</h1>")

def run_server():
    server_address = ('127.0.0.1', 8099)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("=" * 50)
    print("🚀 SERVIDOR WEB DE TESTES RODANDO EM http://127.0.0.1:8099")
    print("Pressione Ctrl + C para encerrar o servidor.")
    print("=" * 50)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Servidor encerrado.")

if __name__ == "__main__":
    run_server()
