# 🛡️ A Tríade CIA — Fundamentos de Segurança da Informação

## O que é a Tríade CIA?

A **Tríade CIA** representa os três pilares fundamentais da segurança da informação:

| Pilar | Nome | Definição |
|-------|------|-----------|
| **C** | Confidencialidade | Somente pessoas autorizadas acessam os dados |
| **I** | Integridade | Dados não são alterados sem autorização |
| **A** | Disponibilidade | Dados estão acessíveis quando necessários |

---

## 🔒 Confidencialidade (Confidentiality)

**Objetivo**: Garantir que informações sejam acessadas apenas por quem tem permissão.

### Ameaças:
- Interceptação de dados (sniffing)
- Acesso não autorizado
- Vazamento de credenciais
- Engenharia social / Phishing

### Controles:
- **Criptografia**: AES, RSA, TLS/SSL
- **Controle de acesso**: ACL, RBAC, MFA
- **Mascaramento**: anonimização de dados sensíveis
- **VPN**: criptografia de tráfego

### Exemplo Prático:
```python
# Criptografia simétrica com Python (Fernet/AES)
from cryptography.fernet import Fernet

# Gerar chave
chave = Fernet.generate_key()
f = Fernet(chave)

# Criptografar
mensagem = b"Dado confidencial: senha123"
criptografado = f.encrypt(mensagem)
print("Criptografado:", criptografado)

# Descriptografar
original = f.decrypt(criptografado)
print("Descriptografado:", original.decode())
```

---

## 🔏 Integridade (Integrity)

**Objetivo**: Garantir que os dados não foram modificados sem autorização.

### Ameaças:
- Ataques Man-in-the-Middle (MITM)
- SQL Injection (modifica banco)
- Ransomware (corrompe arquivos)
- Erros humanos acidentais

### Controles:
- **Hashing**: MD5 (obsoleto), SHA-256, SHA-3
- **Assinatura Digital**: confirma autoria
- **Checksums**: verificação de integridade de arquivos
- **Versionamento**: Git para rastrear mudanças

### Exemplo Prático:
```python
import hashlib

def verificar_integridade(arquivo, hash_esperado):
    sha256 = hashlib.sha256()
    with open(arquivo, 'rb') as f:
        for bloco in iter(lambda: f.read(4096), b''):
            sha256.update(bloco)
    hash_atual = sha256.hexdigest()
    
    if hash_atual == hash_esperado:
        print("✅ Arquivo íntegro!")
    else:
        print("❌ ALERTA: Arquivo foi modificado!")
    return hash_atual

# Gerar hash de um arquivo
texto = b"Conteudo do arquivo de configuracao"
hash_original = hashlib.sha256(texto).hexdigest()
print("Hash SHA-256:", hash_original)
```

---

## ✅ Disponibilidade (Availability)

**Objetivo**: Garantir acesso aos dados sempre que necessário.

### Ameaças:
- DDoS — Distributed Denial of Service
- Falhas de hardware/software
- Desastres naturais
- Ransomware (sequestra acesso)

### Controles:
- **Redundância**: RAID, clusters, backups
- **Load Balancing**: distribuir carga
- **CDN**: conteúdo próximo do usuário
- **Plano de DR (Disaster Recovery)**: RTO e RPO

---

## 🔺 Extensões da Tríade

Modelos modernos adicionam:

| Extensão | Significado |
|----------|-------------|
| **Autenticidade** | Confirma identidade de usuários/sistemas |
| **Não-repúdio** | Ações não podem ser negadas |
| **Privacidade** | Proteção de dados pessoais (LGPD/GDPR) |
| **Responsabilidade** | Rastreabilidade de ações (logs/auditoria) |

> 🎯 **Para Certificações**: A tríade CIA é fundamental para CompTIA Security+, CEH, CISSP e EC-Council CEH.
