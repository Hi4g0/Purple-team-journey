#!/usr/bin/env python3
# =========================================================
# Script: log_analyzer.py
# Descricao: Analisador de Logs para Detecção de Bruteforce (Blue Team)
# Autor: Hiago (Purple Team Journey)
# =========================================================

from collections import defaultdict
import re

# Limite de erros 404 antes de considerar uma ameaça
THRESHOLD_404 = 5

def analyze_logs(log_data):
    print("=" * 60)
    print("🛡️  INICIANDO ANÁLISE DE LOGS - BLUE TEAM SOC MONITOR")
    print("=" * 60)

    # Dicionario para contar erros 404 por IP
    failed_requests = defaultdict(int)
    
    # Expressao regular para extrair IP e Codigo HTTP
    log_pattern = re.compile(r'^(?P<ip>\d+\.\d+\.\d+\.\d+).*?"(?P<method>GET|POST).*?" (?P<status>\d{3})')

    for line in log_data.strip().splitlines():
        match = log_pattern.search(line)
        if match:
            ip = match.group('ip')
            status = match.group('status')

            if status == '404':
                failed_requests[ip] += 1

    print("\n📊 RELATÓRIO DE SUSPEITAS:")
    print("-" * 40)
    
    alerts = 0
    for ip, count in failed_requests.items():
        if count >= THRESHOLD_404:
            print(f"🚨 [ALERTA] IP {ip} detectado realizando Bruteforce/Fuzzing!")
            print(f"   └─ Total de requisições 404 (Não Encontrado): {count}")
            alerts += 1
        else:
            print(f"ℹ️  [NORMAL] IP {ip} possui apenas {count} erros 404.")

    if alerts == 0:
        print("✅ Nenhum comportamento malicioso detectado.")
        
    print("\n=" * 60)

if __name__ == "__main__":
    # Simulacao de Log do Servidor (Baseado nos testes do Gobuster de hoje)
    sample_logs = """
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /backup HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /secret-admin HTTP/1.1" 200 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /admin HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /login HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /uploads HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /test HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /home HTTP/1.1" 404 -
127.0.0.1 - - [30/Jul/2026 00:20:44] "GET /config HTTP/1.1" 404 -
"""
    analyze_logs(sample_logs)
