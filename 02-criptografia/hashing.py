# =====================================================================
# HASHING — Fundamentos e Aplicações
# Uso: python hashing.py
# =====================================================================

import hashlib
import hmac
import os
import time

print("=" * 60)
print("     DEMONSTRAÇÃO DE HASHING")
print("=" * 60)

# ── 1. Algoritmos básicos ─────────────────────────────────────────────
mensagem = "Eduardo Junior — Cybersecurity Student"
mensagem_bytes = mensagem.encode('utf-8')

print("\n1. Comparação de Algoritmos de Hash")
print(f"   Texto: '{mensagem}'")
print(f"   MD5    (128 bits): {hashlib.md5(mensagem_bytes).hexdigest()}")
print(f"   SHA-1  (160 bits): {hashlib.sha1(mensagem_bytes).hexdigest()}")
print(f"   SHA-256(256 bits): {hashlib.sha256(mensagem_bytes).hexdigest()}")
print(f"   SHA-512(512 bits): {hashlib.sha512(mensagem_bytes).hexdigest()[:64]}...")
print(f"   SHA3-256:          {hashlib.sha3_256(mensagem_bytes).hexdigest()}")

# ── 2. Efeito Avalanche ────────────────────────────────────────────────
print("\n2. Efeito Avalanche (pequena mudança = hash totalmente diferente)")
msg1 = "senha123"
msg2 = "senha124"  # apenas 1 caractere diferente!
h1 = hashlib.sha256(msg1.encode()).hexdigest()
h2 = hashlib.sha256(msg2.encode()).hexdigest()
print(f"   SHA-256('{msg1}'): {h1}")
print(f"   SHA-256('{msg2}'): {h2}")
# Conta bits diferentes
bits_diferentes = bin(int(h1, 16) ^ int(h2, 16)).count('1')
print(f"   Bits diferentes: {bits_diferentes}/256 ({bits_diferentes/256*100:.1f}%)")

# ── 3. Salting para senhas ─────────────────────────────────────────────
print("\n3. Hash com Salt (proteção contra Rainbow Tables)")

def hash_senha(senha, salt=None):
    if salt is None:
        salt = os.urandom(32)  # 32 bytes aleatórios
    hash_val = hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100000)
    return salt.hex(), hash_val.hex()

def verificar_senha(senha, salt_hex, hash_esperado):
    salt = bytes.fromhex(salt_hex)
    hash_val = hashlib.pbkdf2_hmac('sha256', senha.encode(), salt, 100000)
    return hash_val.hex() == hash_esperado

# Armazenar senha
salt_hex, hash_armazenado = hash_senha("MinhaSenha@2024!")
print(f"   Salt:  {salt_hex[:32]}...")
print(f"   Hash:  {hash_armazenado[:32]}...")

# Verificar login
print(f"   Login correto:   {verificar_senha('MinhaSenha@2024!', salt_hex, hash_armazenado)}")
print(f"   Login incorreto: {verificar_senha('senha_errada', salt_hex, hash_armazenado)}")

# ── 4. HMAC — Autenticação de Mensagens ────────────────────────────────
print("\n4. HMAC — Hash-based Message Authentication Code")
chave_secreta = b"chave_compartilhada_secreta"
mensagem_api = b'{"acao": "transferir", "valor": 1000, "destino": "123456"}'

mac = hmac.new(chave_secreta, mensagem_api, hashlib.sha256).hexdigest()
print(f"   Mensagem: {mensagem_api.decode()}")
print(f"   HMAC-SHA256: {mac}")

# Verificar integridade
mensagem_alterada = b'{"acao": "transferir", "valor": 9999, "destino": "654321"}'
mac_alterado = hmac.new(chave_secreta, mensagem_alterada, hashlib.sha256).hexdigest()
print(f"   \n   MAC original:  {mac[:32]}...")
print(f"   MAC alterado:  {mac_alterado[:32]}...")
print(f"   Mensagem integra: {mac == mac_alterado}")

# ── 5. Verificação de integridade de arquivos ─────────────────────────
print("\n5. Verificação de integridade de arquivos")
conteudo = b"Conteudo de um arquivo de configuracao importante"
hash_original = hashlib.sha256(conteudo).hexdigest()
print(f"   Hash original:    {hash_original[:40]}...")

conteudo_modificado = conteudo + b"\n# configuracao maliciosa"
hash_modificado = hashlib.sha256(conteudo_modificado).hexdigest()
print(f"   Hash modificado:  {hash_modificado[:40]}...")
print(f"   Integro: {hash_original == hash_modificado}")

print("\n" + "=" * 60)
print("✅ Demonstração concluída!")
print("=" * 60)
