# 🌐 Análise de Redes e Segurança — Guia Prático

## Modelo OSI e Segurança por Camada

| Camada | Nome | Protocolo | Ameaças | Defesas |
|--------|------|-----------|---------|---------|
| 7 | Aplicação | HTTP, DNS, SMTP | XSS, SQLi, MITM | WAF, HTTPS, input validation |
| 6 | Apresentação | TLS, SSL | Downgrade attacks | TLS 1.3, HSTS |
| 5 | Sessão | NetBIOS, RPC | Session Hijacking | Secure cookies, MFA |
| 4 | Transporte | TCP, UDP | SYN Flood, Port Scan | Firewall, rate limiting |
| 3 | Rede | IP, ICMP | IP Spoofing, DDoS | ACL, IPS, BGP filtering |
| 2 | Enlace | Ethernet, ARP | ARP Spoofing, CAM Flood | DAI, port security |
| 1 | Física | Cabos, WiFi | Tap físico, Evil Twin | Segurança física, WPA3 |

---

## 🔍 Comandos Essenciais de Diagnóstico

### Windows
```cmd
:: Ver conexões ativas
netstat -an | findstr ESTABLISHED

:: Ver tabela ARP (possível ARP Spoofing?)
arp -a

:: Ver rota de pacotes
tracert 8.8.8.8

:: Informações DNS
nslookup google.com 8.8.8.8

:: Escanear portas abertas localmente
netstat -ano | findstr LISTENING
```

### Linux / Kali
```bash
# Informações de interface de rede
ip addr show
ifconfig

# Conexões ativas com PID
ss -tulnp

# Monitorar tráfego em tempo real
tcpdump -i eth0 -n -v

# Análise com nmap (somente em redes autorizadas)
nmap -sV -O 192.168.1.0/24

# Ver tabela ARP
arp -n
ip neigh show
```

---

## 🔒 TLS/SSL — Como o HTTPS funciona

```
Cliente                              Servidor
  |                                      |
  |──── ClientHello (TLS 1.3) ─────────>|
  |<─── ServerHello + Certificado ───────|
  |                                      |
  |  [Verifica certificado com CA]       |
  |                                      |
  |──── Key Exchange (ECDHE) ──────────>|
  |<─── Finished ────────────────────────|
  |                                      |
  |═══════ Dados Criptografados ══════════|
  |                        (AES-256-GCM) |
```

### Verificar certificado TLS
```bash
# Ver detalhes do certificado de um site
openssl s_client -connect github.com:443 -showcerts 2>/dev/null | openssl x509 -text

# Verificar data de expiração
echo | openssl s_client -servername google.com -connect google.com:443 2>/dev/null | \
openssl x509 -noout -dates
```

---

## 🛡️ Segurança WiFi — WPA3 vs WPA2

| Característica | WPA2-Personal | WPA3-Personal |
|----------------|---------------|---------------|
| Handshake | 4-way (PSK) | SAE (Dragonfly) |
| Vulnerável a | PMKID, KRACK | N/A |
| Força de senha | Crítico | Resistente a dict. attack |
| Forward Secrecy | ❌ | ✅ |
| PMF | Opcional | Obrigatório |

---

## 🔐 Firewall — Regras Básicas

```bash
# Linux — iptables
# Bloquear todo tráfego de entrada
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Permitir loopback
iptables -A INPUT -i lo -j ACCEPT

# Permitir conexões estabelecidas
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Permitir SSH (porta 22) apenas de IP específico
iptables -A INPUT -p tcp --dport 22 -s 192.168.1.100 -j ACCEPT

# Permitir HTTP e HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Salvar regras
iptables-save > /etc/iptables/rules.v4
```

---

## 📊 Ferramentas de Segurança de Rede

| Ferramenta | Uso | Categoria |
|-----------|-----|-----------|
| **Wireshark** | Análise de pacotes (GUI) | Sniffer |
| **tcpdump** | Captura de pacotes (CLI) | Sniffer |
| **nmap** | Port scanning, fingerprinting | Recon |
| **Metasploit** | Framework de exploração | Pentest |
| **Burp Suite** | Proxy e análise web | Web Sec |
| **John the Ripper** | Cracking de hashes | Password |
| **Aircrack-ng** | Análise de WiFi | Wireless |
| **Snort/Suricata** | IDS/IPS | Defesa |

> ⚠️ **Importante**: Todas estas ferramentas devem ser usadas APENAS em ambientes autorizados (próprios, laboratórios, CTFs). O uso não autorizado é crime.
