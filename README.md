# Network Lab

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![GNS3](https://img.shields.io/badge/GNS3-2.2+-blue.svg)
![Cisco](https://img.shields.io/badge/Cisco-IOS-orange.svg)
![Network](https://img.shields.io/badge/networking-lab-green.svg)

## 🌐 Descrição

Laboratório completo de redes desenvolvido para estudo e simulação de topologias reais. Este repositório contém projetos GNS3, configurações de equipamentos e documentação para implementação de diferentes cenários de rede.

## 🎯 Objetivos do Laboratório

- Simulação de topologias LAN e WAN reais
- Configuração de protocolos de roteamento
- Implementação de serviços de rede (DHCP, DNS, NAT)
- Testes de conectividade e troubleshooting
- Laboratórios de segurança de rede
- Cenários de alta disponibilidade

## 📁 Estrutura do Projeto

```
network-lab/
├── gns3/
│   ├── topologies/
│   │   ├── basic-lan/
│   │   │   ├── basic-lan.gns3
│   │   │   └── configs/
│   │   ├── enterprise-wan/
│   │   │   ├── enterprise-wan.gns3
│   │   │   └── configs/
│   │   ├── mpls-vpn/
│   │   └── datacenter/
│   └── images/
├── configs/
│   ├── routers/
│   ├── switches/
│   ├── firewalls/
│   └── services/
│       ├── dhcp/
│       ├── dns/
│       └── web/
├── scripts/
│   ├── auto-config.py
│   ├── backup-configs.sh
│   └── topology-validator.py
├── docs/
│   ├── lab-guides/
│   ├── troubleshooting/
│   └── protocols/
└── README.md
```

## 🔧 Topologias Disponíveis

### 🏢 Rede LAN Básica (basic-lan.gns3)
**Cenário**: Pequena empresa com departamentos separados
- **Equipamentos**: 3 switches, 1 router, 6 PCs
- **VLANs**: Administração (10), Vendas (20), TI (30)
- **Protocolos**: DHCP, DNS interno, Inter-VLAN routing
- **Serviços**: File server, print server

```
Topologia:
Internet
   |
Router-GW (10.0.0.1)
   |
Switch-Core
   |
├── Switch-Admin (VLAN 10: 192.168.10.0/24)
├── Switch-Sales (VLAN 20: 192.168.20.0/24)
└── Switch-IT (VLAN 30: 192.168.30.0/24)
```

### 🌍 Rede WAN Empresarial (enterprise-wan.gns3)
**Cenário**: Matriz conectada a 3 filiais
- **Protocolos**: OSPF, BGP, MPLS
- **Links**: Frame Relay, VPN IPSec
- **Redundância**: Multiple paths, failover
- **QoS**: Traffic shaping, prioritization

```
Topologia:
Matriz (SP) ←→ ISP-1 ←→ Internet ←→ ISP-2 ←→ Filial-RJ
    ↕                                        ↕
Filial-MG ←←←←←← MPLS Network ←←←←←← Filial-RS
```

### 🏭 Datacenter Network (datacenter.gns3)
**Cenário**: Infraestrutura de datacenter
- **Arquitetura**: Spine-Leaf topology
- **Protocolos**: BGP, EVPN, VXLAN
- **Load Balancing**: ECMP, LAG
- **Virtualização**: Network overlay

### 🔒 Security Lab (security-lab.gns3)
**Cenário**: Testes de segurança de rede
- **Equipamentos**: Firewalls, IDS/IPS
- **Segmentação**: DMZ, Internal, External
- **Testes**: Penetration testing, vulnerability assessment

## ⚡ Configuração do Ambiente

### Pré-requisitos
```bash
# Instalar GNS3
sudo add-apt-repository ppa:gns3/ppa
sudo apt update
sudo apt install gns3-gui gns3-server

# Dependências adicionais
sudo apt install wireshark dynamips vpcs
```

### Configuração Inicial
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/network-lab.git
cd network-lab

# Configurar images path no GNS3
# File > Preferences > Server > Images directory
```

### Images Necessárias
```bash
# Cisco IOS (exemplo)
c7200-advipservicesk9-mz.152-4.S5.bin

# Switches
vios_l2-adventerprisek9-m.SSA.high_iron_20190423.qcow2

# Linux para serviços
ubuntu-server-20.04.qcow2
```

## 🚀 Como Usar

### Carregar Topologia
```bash
# Abrir projeto no GNS3
gns3 gns3/topologies/basic-lan/basic-lan.gns3

# Ou pela interface gráfica:
# File > Open Project > Selecionar arquivo .gns3
```

### Configuração Automática
```bash
# Usar script de auto-configuração
python3 scripts/auto-config.py --topology basic-lan

# Aplicar configurações manualmente
# Copiar configs da pasta configs/ para cada dispositivo
```

### Validar Conectividade
```bash
# Script de validação
python3 scripts/topology-validator.py --test basic-lan

# Testes manuais no GNS3
# Usar console dos dispositivos
# Ping entre hosts, traceroute, etc.
```

## 📋 Laboratórios Práticos

### Lab 1: Configuração VLAN Básica
**Objetivo**: Implementar VLANs e inter-VLAN routing
```bash
# Cenário: basic-lan topology
# Tempo estimado: 2 horas
# Pré-requisitos: Conhecimento básico de switching
```

**Passos**:
1. Configurar VLANs nos switches
2. Configurar trunk ports
3. Implementar DHCP por VLAN
4. Configurar roteamento entre VLANs
5. Testar conectividade

### Lab 2: Roteamento OSPF
**Objetivo**: Implementar OSPF em topologia multi-área
```bash
# Cenário: enterprise-wan topology
# Tempo estimado: 3 horas
# Pré-requisitos: Conhecimento de roteamento
```

### Lab 3: VPN IPSec Site-to-Site
**Objetivo**: Conectar filiais via VPN
```bash
# Cenário: Modificar enterprise-wan
# Tempo estimado: 4 horas
# Pré-requisitos: Conhecimento de criptografia
```

### Lab 4: QoS Implementation
**Objetivo**: Implementar qualidade de serviço
```bash
# Cenário: Qualquer topologia WAN
# Tempo estimado: 2 horas
# Pré-requisitos: Conceitos de QoS
```

## 🔧 Configurações Pré-definidas

### Router Principal (R1)
```cisco
hostname Router-Gateway
!
interface GigabitEthernet0/0
 description WAN Interface
 ip address 200.1.1.1 255.255.255.252
 no shutdown
!
interface GigabitEthernet0/1
 description LAN Interface
 ip address 192.168.1.1 255.255.255.0
 no shutdown
!
ip route 0.0.0.0 0.0.0.0 200.1.1.2
!
access-list 1 permit 192.168.1.0 0.0.0.255
ip nat inside source list 1 interface GigabitEthernet0/0 overload
```

### Switch Core (SW1)
```cisco
hostname Switch-Core
!
vlan 10
 name Administration
vlan 20
 name Sales
vlan 30
 name IT
!
interface range FastEthernet0/1-8
 switchport mode access
 switchport access vlan 10
!
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20,30
```

### Servidor DHCP (Linux)
```bash
# /etc/dhcp/dhcpd.conf
subnet 192.168.10.0 netmask 255.255.255.0 {
    range 192.168.10.100 192.168.10.200;
    option routers 192.168.10.1;
    option domain-name-servers 8.8.8.8;
}
```

## 🔍 Monitoramento e Troubleshooting

### Comandos Úteis de Diagnóstico
```cisco
# Verificar status das interfaces
show ip interface brief

# Tabela de roteamento
show ip route

# Protocolos de roteamento
show ip ospf neighbor
show ip ospf database

# VLANs e trunks
show vlan brief
show interfaces trunk

# NAT translations
show ip nat translations
```

### Captura de Pacotes
```bash
# Configurar wireshark no GNS3
# Clicar direito no link > Start capture

# Analisar tráfego específico
# Filter: tcp.port == 80
# Filter: ospf or rip
```

### Scripts de Monitoramento
```bash
# Monitor de conectividade
./scripts/ping-monitor.sh --topology basic-lan

# Análise de performance
./scripts/performance-test.py --target all-devices

# Backup automático de configurações
./scripts/backup-configs.sh --daily
```

## 📄 Licença

Este projeto está licenciado sob a Licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👨‍💻 Autor

**Vinicius Moreira**
- GitHub: [@Viniciuss-Moreira](https://github.com/Viniciuss-Moreira)
- LinkedIn: [Vinicius Moreira](https://linkedin.com/in/viniciusmoreira-)
- Email: vinnismoreira@gmail.com
