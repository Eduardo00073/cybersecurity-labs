# Criptografia — Conceitos Essenciais

## Tipos de Criptografia

### 🔑 Simétrica
Uma única chave para criptografar E descriptografar.

**Vantagens**: Rápida, eficiente para grandes volumes
**Desvantagens**: Distribuição segura da chave é difícil

**Algoritmos**: AES (128/256 bits), DES, 3DES, Blowfish

### 🔐 Assimétrica
Par de chaves: pública (criptografa) + privada (descriptografa).

**Vantagens**: Não precisa compartilhar a chave privada
**Desvantagens**: Mais lenta que simétrica

**Algoritmos**: RSA, ECC, Diffie-Hellman

### #️⃣ Hash (Resumo)
Transforma dados em um resumo de tamanho fixo. **Não é reversível**.

**Uso**: Verificar integridade, armazenar senhas
**Algoritmos**: SHA-256, SHA-512, MD5 (obsoleto), bcrypt (senhas)

## Certificados Digitais

Um certificado digital associa uma chave pública a uma identidade, validado por uma Autoridade Certificadora (CA).

**Uso principal**: HTTPS (SSL/TLS) — o cadeado no navegador!

**Fluxo**:
1. Servidor gera par de chaves
2. Envia chave pública para a CA
3. CA valida identidade e emite certificado
4. Navegador verifica o certificado ao acessar o site
