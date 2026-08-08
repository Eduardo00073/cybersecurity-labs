# =====================================================================
# CRIPTOGRAFIA SIMÉTRICA — AES e Fernet
# Instale: pip install cryptography
# =====================================================================

try:
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.backends import default_backend
    import os
    import base64

    print("=" * 60)
    print("     CRIPTOGRAFIA SIMÉTRICA")
    print("=" * 60)

    # ── 1. Fernet (AES-128-CBC + HMAC-SHA256) ─────────────────────────
    print("\n1. Fernet (AES-128 + HMAC — Recomendado para uso geral)")
    
    # Gerar chave
    chave = Fernet.generate_key()
    print(f"   Chave gerada: {chave[:30].decode()}...")
    
    f = Fernet(chave)
    
    # Criptografar
    dados_sensiveis = "CPF: 123.456.789-01 | Cartão: 4532-xxxx-xxxx-1234"
    criptografado = f.encrypt(dados_sensiveis.encode())
    print(f"   Original:     {dados_sensiveis}")
    print(f"   Criptografado: {criptografado[:50].decode()}...")
    
    # Descriptografar
    descriptografado = f.decrypt(criptografado).decode()
    print(f"   Descriptografado: {descriptografado}")
    
    # ── 2. AES-256-GCM (modo autenticado) ─────────────────────────────
    print("\n2. AES-256-GCM (modo autenticado — padrão da indústria)")
    
    def aes_gcm_encrypt(plaintext: bytes, key: bytes) -> tuple:
        iv = os.urandom(12)  # 96 bits IV para GCM
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        return iv, ciphertext, encryptor.tag

    def aes_gcm_decrypt(iv: bytes, ciphertext: bytes, tag: bytes, key: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()

    chave_aes = os.urandom(32)  # AES-256 = 32 bytes
    mensagem = b"Mensagem ultra secreta - AES-256-GCM!"
    
    iv, cipher_text, tag = aes_gcm_encrypt(mensagem, chave_aes)
    print(f"   IV:         {iv.hex()}")
    print(f"   Cipher:     {cipher_text.hex()[:40]}...")
    print(f"   Tag (auth): {tag.hex()}")
    
    plaintext = aes_gcm_decrypt(iv, cipher_text, tag, chave_aes)
    print(f"   Decryptado: {plaintext.decode()}")
    
    # ── 3. Comparação AES vs RSA ──────────────────────────────────────
    print("\n3. Quando usar cada um?")
    print("""
   +─────────────────────┬───────────────────────────────────────+
   │ Critério            │ Simétrico (AES)   │ Assimétrico (RSA) │
   +─────────────────────┼───────────────────┼───────────────────+
   │ Velocidade          │ ⚡ Muito rápido    │ 🐢 Lento           │
   │ Chave               │ 1 chave secreta   │ Par público/privado│
   │ Troca de chave      │ ❌ Problema        │ ✅ Resolvido        │
   │ Tamanho de chave    │ 128-256 bits      │ 2048-4096 bits     │
   │ Uso ideal           │ Dados em volume   │ Troca de chaves    │
   +─────────────────────┴───────────────────┴───────────────────+
   
   Solução: HÍBRIDO — RSA troca a chave AES, AES criptografa os dados!
   Exatamente como funciona HTTPS/TLS!
    """)

except ImportError:
    print("Instale: pip install cryptography")
    print("Conceitos (sem dependência):")
    print("- AES: Advanced Encryption Standard, bloco de 128 bits")
    print("- Modos: CBC, GCM, CTR (GCM é autenticado!)")
    print("- Chaves: 128, 192 ou 256 bits")
    print("- IV: Vetor de Inicialização, único por mensagem")
