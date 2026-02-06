# 📁 ARP_MITM_Scapy

## 📌 Descripción

Este repositorio contiene un script que realiza un ataque **Man-in-the-Middle (MITM)** mediante **ARP Spoofing**, permitiendo interceptar el tráfico entre una víctima y el gateway.

---

## 🎯 Objetivo del Script

✅ Envenenar la tabla ARP de la víctima y del gateway  
✅ Redirigir el tráfico a través del atacante  
✅ Demostrar la vulnerabilidad del protocolo ARP  

---

## 🧪 Entorno de Pruebas

| Componente | Valor |
|-----------|-------|
| **Plataforma** | PNETLab |
| **Atacante** | Kali Linux |
| **Víctima** | Windows |
| **Gateway** | Router |
| **Protocolo atacado** | ARP |

---

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
| 10 | Vlan10 | VLAN de laboratorio para pruebas de seguridad |

---

## 🌐 Direccionamiento IP por VLAN

### VLAN 10 – 12.0.0.0/24

| Dispositivo | Interfaz | IP |
|------------|----------|-----|
| Router | e0/0.10 | 12.0.0.1 |
| Switch | VLAN 10 | — |
| Kali Linux | eth0 | 12.0.0.10 |
| Windows | eth0 | 12.0.0.20 |

---

## ⚙️ Requisitos

- ✅ Kali Linux
- ✅ Python 3
- ✅ Scapy
- ✅ IP Forwarding habilitado
- ✅ Víctima y atacante en la misma VLAN

---

## 🔧 Configuración previa

### Habilitar IP Forwarding

```bash
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
```

### Verificar:

```bash
cat /proc/sys/net/ipv4/ip_forward
```

Debe retornar `1`

---

## ▶️ Uso del Script

```bash
sudo python3 script.py
```

---

## 📄 Script: `arp_mitm.py`

El script se encuentra en el archivo [`script.py`](./script.py)

---

## 📸 Evidencia del Ataque

### Topología

<img width="484" height="473" alt="image" src="https://github.com/user-attachments/assets/c03d4bd3-9345-492d-abc1-cf43bda95427" />

### Ejecución del Script

<img width="212" height="67" alt="image" src="https://github.com/user-attachments/assets/1dbd4b0c-ebe0-4a5e-99b0-a12c49b1ef70" />

### Resultado del Ataque

<img width="435" height="201" alt="image" src="https://github.com/user-attachments/assets/d8353614-751e-4e0c-aad9-6bec132630b7" />

---

## ✔️ Verificación

### En Windows:

```cmd
arp -a
```

### Resultado esperado:

La IP del gateway (`12.0.0.1`) aparece con la **MAC de Kali** en lugar de la MAC real del router.

---

## 🛡️ Medidas de Mitigación

| Medida | Descripción |
|--------|-------------|
| **Dynamic ARP Inspection (DAI)** | Valida paquetes ARP contra la tabla DHCP Snooping |
| **DHCP Snooping** | Protege contra ataques DHCP maliciosos |
| **Segmentación por VLAN** | Aisla dispositivos críticos |
| **Protocolos cifrados** | Uso de HTTPS, SSH, VPN |
| **Monitoreo ARP anómalo** | Detecta cambios sospechosos en la tabla ARP |

---

## ⚠️ Advertencia Legal

Este script es **únicamente con fines educativos**. El uso no autorizado de técnicas de hacking es ilegal. Asegúrate de tener permiso explícito antes de realizar pruebas de seguridad.

---

## 📚 Referencias

- [Scapy Documentation](https://scapy.readthedocs.io/)
- [ARP Spoofing - OWASP](https://owasp.org/)
- [PNETLab](https://pnetlab.com/)

---

## 👤 Autor

**Mariana Doñe Lara**

---

## 📝 Licencia

Este proyecto está bajo fines educativos. Úsalo responsablemente.
