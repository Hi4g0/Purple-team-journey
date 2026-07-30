#!/usr/bin/env python3
# =========================================================
# Script: log_analyzer.py
# Descricao: Analisador de Logs para Detecção de Bruteforce/Fuzzing
# Autor: Hiago (Purple Team Journey)
# =========================================================

from collections import defaultdict
import re
import os

# Limite de erros 404 para considerar um ataque
THRESHOLD_404 = 5

def analyze_logs(log_data):
    print("=" * 60)
    print("🛡️  INICIANDO ANÁLISE DE LOGS - BLUE TEAM SOC MONITOR")
    print("=" * 60)

    failed_requests = defaultdict(int)
    
    # Expressao regular para extrair IP, metodo HTTP e codigo de status
    log_pattern = re.compile(r'^(?P<ip>\d+\.\d+\.\d+\.\d+).*?"(?P<method>GET|POST).*?" (?P<status>\d{3})')

    for line in log_data.strip().splitlines():
        match = log_pattern.search(line)
        if match:
            ip = match.group('ip')
            status = match.group('status')

            if status == '404':
                failed_requests[ip] += 1

    print("\n📊 RELATÓRIO DE AMEAÇAS DETECTADAS:")
    print("-" * 40)
    
    alerts = 0
    for ip, count in failed_requests.items():
        if count >= THRESHOLD_404:
            print(f"🚨 [ALERTA DISPARADO] IP {ip} ultrapassou o limite de seguranca!")
            print(f"   └─ Motivo: Suspeita de Directory Fuzzing ({count} respostas 404 registradas)")
            alerts += 1
        else:
            print(f"ℹ️  [TRÁFEGO NORMAL] IP {ip} possui {count} erros 404.")

    if alerts == 0:
        print("✅ Nenhum comportamento malicioso detectado ate o momento.")
        
    print("\n=" * 60)

if __name__ == "__main__":
    log_filename = "access.log"
    
    if os.path.exists(log_filename):
        with open(log_filename, "r") as f:
            logs = f.read()
            if logs.strip():
                analyze_logs(logs)
            else:
                print("[-] O arquivo access.log esta vazio. Gere trafego no servidor primeiro!")
    else:
        print(f"[-] Arquivo '{log_filename}' nao encontrado.")
        print("💡 Inicie o servidor (web_server.py) e execute o ataque (dir_fuzzer.py) primeiro.")
