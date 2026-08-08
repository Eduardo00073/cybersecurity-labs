# Checklist de Hardening de Sistemas

## 🖥️ Sistema Operacional
- [ ] Manter sistema atualizado (patches de segurança)
- [ ] Desabilitar serviços desnecessários
- [ ] Configurar firewall local
- [ ] Desabilitar login root remoto
- [ ] Configurar política de senhas fortes
- [ ] Habilitar logs de auditoria

## 🌐 Rede
- [ ] Alterar portas padrão de serviços críticos
- [ ] Usar SSH ao invés de Telnet
- [ ] Configurar fail2ban (bloqueio após tentativas)
- [ ] Segmentar rede (VLANs)
- [ ] Usar VPN para acessos remotos
- [ ] Desabilitar protocolos inseguros (FTP, HTTP)

## 🔑 Autenticação
- [ ] Implementar autenticação multifator (2FA/MFA)
- [ ] Política de senhas: mínimo 12 caracteres, complexidade
- [ ] Rotação periódica de credenciais
- [ ] Princípio do menor privilégio
- [ ] Revogar acessos de ex-funcionários imediatamente

## 💾 Dados
- [ ] Criptografar dados em repouso e em trânsito
- [ ] Backup automatizado (regra 3-2-1)
- [ ] Testar restauração de backups regularmente
- [ ] Classificar dados por sensibilidade
