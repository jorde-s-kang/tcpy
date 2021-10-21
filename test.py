import tap
from EthernetFrame import EthernetFrame

tun = tap.make_tun("tap0")
pkts = tap.read_pkts(tun, 10)
print("packets read:")
for pkt in pkts:
    print(EthernetFrame(pkt))
