# README for ARP MITM Scapy Project

## Entorno de Pruebas

... (existing content) ...

## 📡 VLANs utilizadas en el laboratorio

### 🟦 VLAN 10 – LAN Laboratorio

Se configuró una única VLAN para garantizar la comunicación directa entre los hosts y permitir la ejecución de ataques de Capa 2.

#### 📌 Motivo

- ARP es un protocolo de Capa 2
- CDP opera únicamente dentro del mismo dominio de broadcast
- Los ataques MITM y CDP DoS NO atraviesan VLANs

#### 📋 Detalle de la VLAN

| VLAN ID | Nombre | Descripción |
|---------|--------|-------------|
| 10 | LAN-LAB | VLAN de laboratorio para pruebas de seguridad |

### 🌐 Direccionamiento IP por VLAN

#### VLAN 10 – 12.0.0.0/24

| Dispositivo | Interfaz | IP |
|------------|----------|-----|
| Router | e0/0.10 | 12.0.0.1 |
| Switch | VLAN 10 | — |
| Kali Linux | eth0 | 12.0.0.10 |
| Windows | eth0 | 12.0.0.20 |

![red-topologia](https://github.com/mariana121319/ARP_MITM_Scapy/blob/main/topologia-red.png)
![ataque-ejecutandose](https://github.com/mariana121319/ARP_MITM_Scapy/blob/main/ataque-ejecutandose.png)
![verificacion-arp](https://github.com/mariana121319/ARP_MITM_Scapy/blob/main/verificacion-arp.png)