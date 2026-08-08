# 🐧 Kali Linux — Comandos Essenciais para Segurança

> ⚠️ Use somente em ambientes autorizados e controlados. Este guia é educacional.

## 🗂️ Organização do Kali Linux

```
/usr/share/wordlists/    → Wordlists (rockyou.txt, etc.)
/usr/share/metasploit-framework/  → Módulos Metasploit
/usr/share/nmap/scripts/ → Scripts NSE do Nmap
/etc/hosts               → Resolução DNS local
/var/log/                → Logs do sistema
```

## 🔍 Reconhecimento Passivo (OSINT)

```bash
# whois — informações de domínio
whois example.com

# dig — consulta DNS completa
dig example.com ANY
dig example.com MX
dig -x 8.8.8.8  # PTR reverso

# Google Dorks (sem acesso ao alvo!)
# site:example.com filetype:pdf
# inurl:admin site:example.com
# "index of" site:example.com

# theHarvester — coleta de e-mails e subdomínios
theHarvester -d example.com -b google,bing,linkedin

# Shodan CLI (requer conta)
shodan search "apache 2.2 country:BR"
```

## 🔍 Reconhecimento Ativo (somente em redes autorizadas!)

```bash
# Nmap — o canivete suíço do recon
nmap -sn 192.168.1.0/24              # Ping scan (hosts ativos)
nmap -sV 192.168.1.1                 # Detectar versão de serviços
nmap -O 192.168.1.1                  # Detectar OS
nmap -sC -sV -oA saida 192.168.1.1  # Script default + saída multi-formato
nmap -p- 192.168.1.1                 # Todas as 65535 portas
nmap --script vuln 192.168.1.1       # Scripts de vulnerabilidade

# Netcat — conexões TCP/UDP
nc -nvlp 4444          # Escutar na porta 4444
nc -nv 192.168.1.1 80  # Conectar na porta 80

# Ping sweep manual
for i in {1..254}; do ping -c1 -W1 192.168.1.$i &>/dev/null && echo "192.168.1.$i UP"; done
```

## 🔐 Análise de Senhas (em hashes próprios)

```bash
# Hashcat — GPU cracking
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt    # MD5
hashcat -m 1000 hashes.txt rockyou.txt                       # NTLM
hashcat -m 1800 hash.txt rockyou.txt                         # SHA-512 (Unix)

# John the Ripper
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
john --show hash.txt  # Mostrar crackeados

# Identificar tipo de hash
hash-identifier
echo "5f4dcc3b5aa765d61d8327deb882cf99" | hash-identifier
```

## 🌐 Análise Web (somente em sites autorizados)

```bash
# nikto — scanner de vulnerabilidades web
nikto -h http://192.168.1.1

# dirb/gobuster — brute force de diretórios
gobuster dir -u http://192.168.1.1 -w /usr/share/wordlists/dirb/common.txt

# sqlmap — teste de SQL Injection
sqlmap -u "http://site.com/produto?id=1" --dbs
sqlmap -u "http://site.com/produto?id=1" -D banco --tables

# wfuzz — fuzzing web
wfuzz -w wordlist.txt http://site.com/FUZZ
```

## 📊 Análise de Tráfego

```bash
# tcpdump
tcpdump -i eth0 -w captura.pcap         # Capturar e salvar
tcpdump -r captura.pcap                  # Ler captura
tcpdump -i eth0 port 80                  # Filtrar HTTP
tcpdump -i eth0 'tcp flags & tcp-syn != 0'  # Só SYN packets

# Wireshark filters
# http.request.method == "POST"
# tcp.port == 443
# ip.addr == 192.168.1.1
# dns
```

## 🛡️ Hardening do Sistema

```bash
# Verificar serviços em execução
systemctl list-units --type=service --state=running

# Verificar portas abertas
ss -tulnp

# Verificar usuários com shell
cat /etc/passwd | grep -v nologin | grep -v false

# Verificar SUID files (escalação de privilégio)
find / -perm -u=s -type f 2>/dev/null

# Verificar arquivos modificados recentemente
find /etc -mtime -7 -type f 2>/dev/null
```
