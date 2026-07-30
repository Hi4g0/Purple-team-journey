#!/usr/bin/env python3
# =========================================================
# Script: web_server.py
# Descricao: Servidor Web HTTP simples que salva logs no disco
# Autor: Hiago (Purple Team Journey)
# =========================================================

from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    # Sobrescreve o metodo de log para salvar as requisicoes no arquivo access.log
    def log_message(self, format, *args):
        log_entry = f"{self.client_address[0]} - - [{self.log_date_time_string()}] \"{self.requestline}\" {args[0]} -\n"
        
        # Abre o arquivo em modo 'append' (adiciona ao final sem apagar o existente)
        with open("access.log", "a") as log_file:
            log_file.write(log_entry)
            
        super().log_message(format, *args)

    def do_GET(self):
        # Rota secreta de teste
        if self.path == "/secret-admin":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>PAINEL ADMIN RESTRITO - FLAG{PURPLE_TEAM_2026}</h1>")
        else:
            # Rota padrao de erro (404 Not Found)
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"<h1>404 - Pagina Nao Encontrada</h1>")

def run_server():
    server_address = ('127.0.0.1', 8099)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print("=" * 60)
    print("🚀 SERVIDOR WEB RODANDO EM http://127.0.0.1:8099")
    print("📝 Salvando conexoes reais no arquivo: access.log")
    print("Pressione Ctrl + C para encerrar o servidor.")
    print("=" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] Servidor encerrado.")

if __name__ == "__main__":
    run_server()
