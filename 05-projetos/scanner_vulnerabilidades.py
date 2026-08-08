#!/usr/bin/env python3
# =====================================================================
# SCANNER DE VULNERABILIDADES EDUCACIONAL
# Use SOMENTE em sistemas PRÓPRIOS ou com AUTORIZAÇÃO EXPLÍCITA
# =====================================================================

import socket
import sys
import time
import concurrent.futures
from datetime import datetime

class ScannerEducacional:
    """Scanner simples para aprendizado de conceitos de segurança."""
    
    def __init__(self, alvo: str):
        try:
            self.alvo_ip = socket.gethostbyname(alvo)
            self.alvo_nome = alvo
        except socket.gaierror:
            print(f"[ERRO] Não foi possível resolver: {alvo}")
            sys.exit(1)
        
        self.portas_abertas = []
        self.inicio = datetime.now()
    
    def verificar_porta(self, porta: int, timeout: float = 0.5) -> bool:
        """Verifica se uma porta está aberta."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                resultado = s.connect_ex((self.alvo_ip, porta))
                return resultado == 0
        except:
            return False
    
    def obter_banner(self, porta: int) -> str:
        """Tenta capturar o banner do serviço."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((self.alvo_ip, porta))
                s.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                return banner.split('\n')[0][:80] if banner else ""
        except:
            return ""
    
    def identificar_servico(self, porta: int) -> str:
        """Identifica o serviço comum em uma porta."""
        servicos = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 3306: "MySQL", 3389: "RDP",
            5432: "PostgreSQL", 5900: "VNC", 6379: "Redis",
            8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB"
        }
        return servicos.get(porta, "Unknown")
    
    def avaliar_risco(self, porta: int) -> str:
        """Avalia risco básico da porta aberta."""
        alto_risco = {23: "Telnet sem criptografia!",
                      21: "FTP pode expor credenciais",
                      3389: "RDP público é alvo comum de ataques",
                      27017: "MongoDB sem auth exposto!",
                      6379: "Redis sem auth é crítico!"}
        medio_risco = {3306: "MySQL exposto externamente",
                       5432: "PostgreSQL exposto",
                       445: "SMB — vulnerável a EternalBlue"}
        
        if porta in alto_risco:
            return f"⚠️  ALTO: {alto_risco[porta]}"
        elif porta in medio_risco:
            return f"🟡 MÉDIO: {medio_risco[porta]}"
        return "🟢 Info"
    
    def scan_rapido(self, portas: list = None) -> dict:
        """Scan rápido de portas comuns."""
        if portas is None:
            portas = [21, 22, 23, 25, 53, 80, 110, 143, 443,
                      445, 3306, 3389, 5432, 5900, 8080, 8443]
        
        print(f"\n{'='*60}")
        print(f"  🔍 SCANNER EDUCACIONAL — Uso Autorizado Apenas")
        print(f"{'='*60}")
        print(f"  Alvo:   {self.alvo_nome} ({self.alvo_ip})")
        print(f"  Início: {self.inicio.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"  Portas: {len(portas)} a verificar")
        print(f"{'='*60}\n")
        
        resultados = {}
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
            future_to_porta = {executor.submit(self.verificar_porta, p): p for p in portas}
            for future in concurrent.futures.as_completed(future_to_porta):
                porta = future_to_porta[future]
                if future.result():
                    servico = self.identificar_servico(porta)
                    risco = self.avaliar_risco(porta)
                    resultados[porta] = {'servico': servico, 'risco': risco}
                    self.portas_abertas.append(porta)
        
        return resultados
    
    def relatorio(self, resultados: dict):
        """Exibe relatório formatado."""
        duracao = (datetime.now() - self.inicio).total_seconds()
        
        if not resultados:
            print("  ✅ Nenhuma porta aberta encontrada no conjunto testado.")
        else:
            print(f"  {'PORTA':<8} {'SERVIÇO':<15} {'AVALIAÇÃO'}")
            print(f"  {'-'*55}")
            for porta in sorted(resultados.keys()):
                r = resultados[porta]
                print(f"  {str(porta)+'/tcp':<8} {r['servico']:<15} {r['risco']}")
        
        print(f"\n  Portas abertas: {len(self.portas_abertas)}")
        print(f"  Tempo: {duracao:.2f}s")
        print(f"{'='*60}\n")
        print("  ⚠️  AVISO: Use apenas em sistemas autorizados!")
        print("  📚 Este scanner é educacional — não para uso malicioso")


# ── Uso ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Scan do localhost (sempre permitido — é a sua própria máquina)
    alvo = "127.0.0.1"
    
    scanner = ScannerEducacional(alvo)
    resultados = scanner.scan_rapido()
    scanner.relatorio(resultados)
