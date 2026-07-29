#!/usr/bin/env python3
# =========================================================
# Script: log_parser.py
# Descricao: Analisador de Logs de Autenticacao do Linux
# Autor: Hiago (Purple Team Journey)
# =========================================================

# Caminho do arquivo de log do sistema
LOG_FILE = "/var/log/auth.log"

def analisar_logs():
    print("=" * 50)
    print("🔍 INICIANDO ANALISE AUTOMATICA DE LOGS DE SEGURANCA")
    print("=" * 50)

    try:
        # Abre o arquivo em modo de leitura ('r')
        with open(LOG_FILE, "r") as file:
            contador_falhas = 0

            # Le o arquivo linha por linha
            for line in file:
                # Checa se a linha contem palavras-chave de falha
                if "failure" in line.lower() or "failed" in line.lower():
                    contador_falhas += 1
                    print(f"[⚠️ ALERTA DE SEGURANCA] -> {line.strip()}")

            print("-" * 50)
            print(f"📊 RESUMO: Total de tentativas suspeitas encontradas: {contador_falhas}")

    except FileNotFoundError:
        print(f"[-] Erro: O arquivo {LOG_FILE} nao foi encontrado no sistema.")
    except PermissionError:
        print("[-] Erro de Permissao: Execute o script com 'sudo' para ler os logs do sistema.")

if __name__ == "__main__":
    analisar_logs()
