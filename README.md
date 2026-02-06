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

## 📡 Direccionamiento IP

| Dispositivo | IP |
|------------|------|
| Gateway | `12.0.0.1` |
| Víctima (Windows) | `12.0.0.20` |
| Atacante (Kali) | `12.0.0.10` |

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
sudo python3 arp_mitm.py
```

---

## 📄 Script: `arp_mitm.py`

El script se encuentra en el archivo [`arp_mitm.py`](./arp_mitm.py)

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

**mariana121319**

---

## 📝 Licencia

Este proyecto está bajo fines educativos. Úsalo responsablemente.