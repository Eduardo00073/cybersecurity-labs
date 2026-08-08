# Boas Práticas — Senhas e Autenticação

## Criando Senhas Fortes

### ❌ Senhas Fracas
- `123456`, `senha`, `password`
- Nome + data de nascimento: `joao1990`
- Palavras do dicionário: `cachorro`, `futebol`

### ✅ Senhas Fortes
- Mínimo **12 caracteres**
- Mistura de: maiúsculas, minúsculas, números, símbolos
- Sem dados pessoais
- **Passphrase**: `CaféComLeite@Manhã2024!` (fácil de lembrar, difícil de quebrar)

## Gerenciadores de Senhas
- **Bitwarden** (open source, gratuito)
- **KeePass** (offline, portátil)
- **1Password** (pago, excelente UX)

## Autenticação Multifator (2FA/MFA)

### Fatores de Autenticação
1. **Algo que você sabe**: Senha, PIN
2. **Algo que você tem**: Celular, token, smart card
3. **Algo que você é**: Biometria (digital, face, íris)

### Tipos de 2FA
| Método | Segurança | Recomendação |
|--------|-----------|--------------|
| SMS | ⭐⭐ | Evitar (SIM swap) |
| E-mail | ⭐⭐ | Aceitável |
| App (TOTP) | ⭐⭐⭐⭐ | **Recomendado** (Google Authenticator, Authy) |
| Chave física | ⭐⭐⭐⭐⭐ | Melhor (YubiKey, Titan) |
