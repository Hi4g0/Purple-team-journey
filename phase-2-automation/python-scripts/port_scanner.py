#!/usr/bin/env python3
# =========================================================
# Script: port_scanner.py
# Descricao: Testador basico de portas de rede
# Autor: Hiago (Purple Team Journey)
# =========================================================

import socket

# Alvo local (Sua propria maquina ou servidor de testes)
TARGET = "127.0.0.1"
# Portas comuns para testar: 22 (SSH), 80 (HTTP), 443 (HTTPS)
PORTS = [22, 80, 443]

def scan_ports():
    print("=" * 50)
    print(f"🔍 ESCANEANDO ALVO: {TARGET}")
    print("=" * 50)

    for port in PORTS:
        # Cria um socket de rede TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Define um tempo limite de 1 segundo para a conexao nao travar
        s.settimeout(1.0)
        
        # Tenta se conectar a porta
        result = s.connect_ex((TARGET, port))
        
        # Se o resultado for 0, a conexao foi aceita (Porta Aberta)
        if result == 0:
            print(f"[+] Porta {port}: ABERTA 🟢")
        else:
            print(f"[-] Porta {port}: Fechada ou Bloqueada 🔴")
            
        # Fecha a conexao
        s.close()

if __name__ == "__main__":
    scan_ports()
