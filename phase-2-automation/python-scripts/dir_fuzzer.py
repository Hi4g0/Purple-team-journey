#!/usr/bin/env python3
# =========================================================
# Script: dir_fuzzer.py
# Descricao: Ferramenta simples de Directory Fuzzing em Python
# Autor: Hiago (Purple Team Journey)
# =========================================================

import urllib.request
import urllib.error
import sys

def start_fuzzing(target_url, wordlist_path):
    print("=" * 50)
    print(f"🎯 INICIANDO FUZZING EM: {target_url}")
    print(f"📁 USANDO WORDLIST: {wordlist_path}")
    print("=" * 50)

    try:
        # Abre e le a wordlist linha por linha
        with open(wordlist_path, 'r') as file:
            words = file.read().splitlines()
    except FileNotFoundError:
        print(f"[-] Erro: Arquivo '{wordlist_path}' nao encontrado!")
        return

    # Loop para testar cada palavra da lista
    for word in words:
        if not word.strip():
            continue  # Pula linhas em branco
            
        # Monta a URL completa (ex: http://127.0.0.1:8099/admin)
        url = f"{target_url.rstrip('/')}/{word.strip()}"
        
        try:
            # Faz a requisicao HTTP GET
            req = urllib.request.Request(url, headers={'User-Agent': 'PythonFuzzer/1.0'})
            response = urllib.request.urlopen(req)
            
            # Se retornar codigo 200 (Sucesso)
            if response.status == 200:
                print(f"[+] [200 OK] Encontrado: /{word}")
                
        except urllib.error.HTTPError as e:
            # Captura erros HTTP (como 404, 403, 500)
            if e.code != 404:  # Exibe apenas se nao for 404
                print(f"[!] [{e.code}] Rota especial: /{word}")
        except urllib.error.URLError as e:
            print(f"[-] Erro de conexao: {e.reason}")
            break

    print("\n[+] Varredura finalizada!")

if __name__ == "__main__":
    # Configura o alvo e a wordlist locais
    TARGET = "http://127.0.0.1:8099"
    WORDLIST = "wordlist.txt"
    
    start_fuzzing(TARGET, WORDLIST)
