#!/usr/bin/env python3
# =====================================================================
# ANALISADOR DE FORÇA DE SENHAS
# Educacional — para criar senhas mais seguras
# =====================================================================

import re
import math
import string

class AnalisadorSenha:
    """Analisa e avalia a força de senhas."""
    
    # Wordlist de senhas comuns (subset educacional)
    SENHAS_COMUNS = {
        "123456", "password", "123456789", "12345678", "12345",
        "1234567", "1234567890", "qwerty", "abc123", "111111",
        "123123", "admin", "letmein", "welcome", "monkey",
        "1234", "superman", "batman", "dragon", "master",
        "senha", "brasil", "eduardo", "professor",
    }
    
    def avaliar(self, senha: str) -> dict:
        resultado = {
            'senha': '*' * len(senha),
            'comprimento': len(senha),
            'pontos': 0,
            'problemas': [],
            'melhorias': [],
            'entropia': 0,
            'nivel': '',
            'cor': '',
        }
        
        # Verificar senha comum
        if senha.lower() in self.SENHAS_COMUNS:
            resultado['problemas'].append("❌ Senha está na lista das mais comuns!")
            resultado['nivel'] = 'INACEITÁVEL'
            resultado['cor'] = '🔴'
            return resultado
        
        # Critérios
        tem_min = bool(re.search(r'[a-z]', senha))
        tem_mai = bool(re.search(r'[A-Z]', senha))
        tem_num = bool(re.search(r'[0-9]', senha))
        tem_esp = bool(re.search(r'[^A-Za-z0-9]', senha))
        repeticoes = bool(re.search(r'(.)' + '\1{2,}', senha))  # 3+ chars iguais
        sequencial = any(seq in senha.lower() for seq in ['abc','123','qwe','asd'])
        
        # Pontuação
        if len(senha) >= 8:  resultado['pontos'] += 1
        if len(senha) >= 12: resultado['pontos'] += 1
        if len(senha) >= 16: resultado['pontos'] += 1
        if tem_min: resultado['pontos'] += 1
        if tem_mai: resultado['pontos'] += 1
        if tem_num: resultado['pontos'] += 1
        if tem_esp: resultado['pontos'] += 2
        if not repeticoes: resultado['pontos'] += 1
        if not sequencial: resultado['pontos'] += 1
        
        # Penalidades
        if repeticoes:
            resultado['pontos'] -= 1
            resultado['problemas'].append("⚠️  Caracteres repetidos (ex: aaa, 111)")
        if sequencial:
            resultado['pontos'] -= 1
            resultado['problemas'].append("⚠️  Sequências previsíveis (abc, 123, qwe)")
        
        # Melhorias
        if not tem_mai: resultado['melhorias'].append("➕ Adicione letras maiúsculas (A-Z)")
        if not tem_min: resultado['melhorias'].append("➕ Adicione letras minúsculas (a-z)")
        if not tem_num: resultado['melhorias'].append("➕ Adicione números (0-9)")
        if not tem_esp: resultado['melhorias'].append("➕ Adicione símbolos (!@#$%^&*)")
        if len(senha) < 12: resultado['melhorias'].append("➕ Use pelo menos 12 caracteres")
        
        # Calcular entropia
        charset = 0
        if tem_min: charset += 26
        if tem_mai: charset += 26
        if tem_num: charset += 10
        if tem_esp: charset += 32
        if charset > 0:
            resultado['entropia'] = round(len(senha) * math.log2(charset), 1)
        
        # Nível
        p = resultado['pontos']
        if p <= 2:   resultado['nivel'], resultado['cor'] = 'MUITO FRACA', '🔴'
        elif p <= 4: resultado['nivel'], resultado['cor'] = 'FRACA', '🟠'
        elif p <= 6: resultado['nivel'], resultado['cor'] = 'RAZOÁVEL', '🟡'
        elif p <= 8: resultado['nivel'], resultado['cor'] = 'FORTE', '🟢'
        else:        resultado['nivel'], resultado['cor'] = 'MUITO FORTE', '✅'
        
        return resultado
    
    def exibir(self, resultado: dict):
        print(f"\n{'─'*50}")
        print(f"  Senha:    {resultado['senha']}")
        print(f"  Comprimento: {resultado['comprimento']} caracteres")
        print(f"  Entropia: {resultado['entropia']} bits")
        print(f"  Força:  {resultado['cor']} {resultado['nivel']} ({resultado['pontos']} pts)")
        
        if resultado['problemas']:
            print(f"\n  Problemas:")
            for p in resultado['problemas']: print(f"    {p}")
        
        if resultado['melhorias']:
            print(f"\n  Para melhorar:")
            for m in resultado['melhorias']: print(f"    {m}")
        print(f"{'─'*50}")
    
    def gerar_dica(self) -> str:
        """Dica para criar senha segura."""
        return """
  💡 Técnica da Frase-Senha:
     1. Pense em uma frase memorável
     2. Use iniciais + números + símbolos
     
     "Meu gato Mimi tem 3 anos e adora peixe!"
     → MgMt3ae@p!
     
     Ou use passphrase completa:
     "correto-cavalo-bateria-grampo" (92 bits de entropia!)
        """

# ── Demonstração ──────────────────────────────────────────────────────
if __name__ == "__main__":
    analisador = AnalisadorSenha()
    
    print("\n" + "=" * 50)
    print("     🔐 ANALISADOR DE FORÇA DE SENHAS")
    print("=" * 50)
    
    senhas_teste = [
        "123456",
        "senha",
        "Eduardo",
        "Eduardo2024",
        "Edu@rd0!2024",
        "C0rr3t0-Cav@l0-B@t3ri@-Gr4mp0!",
    ]
    
    for senha in senhas_teste:
        resultado = analisador.avaliar(senha)
        analisador.exibir(resultado)
    
    print(analisador.gerar_dica())
