import code
import tap
import time
from EthernetFrame import EthernetFrame


tun = tap.make_tun("tap0")
pkts = tap.read_pkts(tun, 10)
print("Frames read:")
tap.watch_tun(tun)
code.interact(local=locals())    
