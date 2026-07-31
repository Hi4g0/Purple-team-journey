#!/usr/bin/env python3
# =========================================================
# Script: waf_proxy.py
# Descricao: Web Application Firewall (WAF) Simples em Python (Blue Team)
# Autor: Hiago (Purple Team Journey)
# =========================================================

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import re

# Regras de Assinatura de Ataque do WAF (Expressoes Regulares)
ATTACK_PATTERNS = {
    "SQL Injection": [
        r"(\bOR\b|\bAND\b)\s+1=1",
        r"SELECT\s+.*\s+FROM",
        r"UNION\s+SELECT",
        r"--",
        r"/\*.*\*/"
    ],
    "Cross-Site Scripting (XSS)": [
        r"<script.*?>",
        r"javascript:",
        r"onerror\s*=",
        r"onload\s*="
    ],
    "Path Traversal": [
        r"\.\./\.\.",
        r"/etc/passwd",
        r"c:\\windows"
    ]
}

class WAFHandler(BaseHTTPRequestHandler):

    def inspect_payload(self, data_str):
        """ Inspeciona strings recebidas procurando por padroes de ataque """
        decoded_data = urllib.parse.unquote(data_str)
        
        for attack_type, patterns in ATTACK_PATTERNS.items():
            for pattern in patterns:
                if re.search(pattern, decoded_data, re.IGNORECASE):
                    return attack_type, pattern
        return None, None

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Passa o payload pelo inspetor do WAF
        detected_attack, matched_pattern = self.inspect_payload(post_data)

        if detected_attack:
            # 🚨 BLOQUEIO PELO WAF
            print("\n" + "🚨 " * 15)
            print(f"🛑 [WAF - BLOQUEIO EM TEMPO REAL] IP: {self.client_address[0]}")
            print(f"   ├─ Tipo de Ameaca: {detected_attack}")
            print(f"   ├─ Padrao Detectado: {matched_pattern}")
            print(f"   └─ Payload Inspecionado: {post_data}")
            print("🚨 " * 15 + "\n")

            self.send_response(403)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            response_html = f"""
            <!DOCTYPE html>
            <html>
            <head><title>403 - Acesso Bloqueado pelo WAF</title></head>
            <body style="background-color:#1e1e2e; color:#f38ba8; font-family:Arial; text-align:center; padding-top:50px;">
                <h1>🛡️ 403 FORBIDDEN - REQUISICAO BLOQUEADA</h1>
                <p>O Firewall de Aplicacao Web (WAF) detectou um padrao de ataque malicioso ({detected_attack}).</p>
                <hr style="width:50%; border-color:#f38ba8;">
                <p><small>IP Registrado: {self.client_address[0]} | Incidente logado para auditoria SOC.</small></p>
            </body>
            </html>
            """
            self.wfile.write(response_html.encode('utf-8'))
        else:
            # ✅ REQUISIÇÃO LIMPA - LIBERADA
            print(f"✅ [WAF - TRAFEGO SEGURO] Requisicao aprovada para IP: {self.client_address[0]}")
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            response_html = "<h1>✅ 200 OK - Requisicao Limpa Processada com Sucesso!</h1>"
            self.wfile.write(response_html.encode('utf-8'))

    def do_GET(self):
        # Exibe a interface de teste do WAF
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        html_page = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Lab Purple Team - Teste de WAF</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #1e1e2e; color: #cdd6f4; text-align: center; padding-top: 50px; }
                .card { background-color: #313244; display: inline-block; padding: 30px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.5); }
                input { margin: 10px; padding: 10px; width: 80%; border-radius: 5px; border: none; }
                button { padding: 10px 20px; background-color: #a6e3a1; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; color: #11111b; }
            </style>
        </head>
        <body>
            <div class="card">
                <h2>🛡️ Laboratorio de Testes de WAF</h2>
                <p>Envie entradas normais ou payloads para testar a deteccao:</p>
                <form action="/" method="POST">
                    <input type="text" name="data" placeholder="Digite um texto ou payload de ataque..." required><br>
                    <button type="submit">Enviar Requisicao</button>
                </form>
            </div>
        </body>
        </html>
        """
        self.wfile.write(html_page.encode('utf-8'))

def run_waf():
    server_address = ('127.0.0.1', 8099)
    httpd = HTTPServer(server_address, WAFHandler)
    print("=" * 60)
    print("🛡️  FIREWALL DE APLICACAO WEB (WAF) ATIVO EM http://127.0.0.1:8099")
    print("📝 Inspecionando payloads contra SQLi, XSS e Path Traversal...")
    print("Pressione Ctrl + C para encerrar.")
    print("=" * 60)
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[-] WAF encerrado.")

if __name__ == "__main__":
    run_waf()

