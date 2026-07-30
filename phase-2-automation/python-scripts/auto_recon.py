#!/usr/bin/env python3
# =========================================================
# Script: auto_recon.py
# Descricao: Script de Reconhecimento Automatizado de Serviços
# Autor: Hiago (Purple Team Journey)
# =========================================================

import socket
import sys

def auto_recon(target_host, target_port):
    print("=" * 50)
    print(f"🎯 INICIANDO RECON EM: {target_host}:{target_port}")
    print("=" * 50)
    
    # 1. Teste de Conexao de Porta (Socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2.0)
    
    result = sock.connect_ex((target_host, target_port))
    
    if result == 0:
        print(f"[+] Status: Porta {target_port} está ABERTA 🟢")
        
        # 2. Tentativa de Captura de Banner (HTTP Header)
        try:
            request = f"GET / HTTP/1.1\r\nHost: {target_host}\r\nUser-Agent: PurpleTeamRecon/1.0\r\n\r\n"
            sock.send(request.encode())
            response = sock.recv(1024).decode(errors='ignore')
            
            print("\n🔍 RESPOSTA DO SERVIDOR (BANNER/HEADER):")
            print("-" * 40)
            # Exibe as primeiras linhas da resposta
            print("\n".join(response.splitlines()[:5]))
            print("-" * 40)
            
        except Exception as e:
            print(f"[-] Nao foi possivel capturar o banner: {e}")
            
    else:
        print(f"[-] Status: Porta {target_port} está FECHADA ou INACESSÍVEL 🔴")
        
    sock.close()

if __name__ == "__main__":
    # Testa a porta 8099 onde seu servidor Python roda
    auto_recon("127.0.0.1", 8099)
