# An interface for the Linux Universal TUN/TAP Driver, for "tapping"
# level 3 (TUN) and level 2 (TAP) IP or Ethernet packets.


import EthernetFrame as e
import code
import os
import threading
import socket
import fcntl
import struct
import subprocess

def make_tun(iface):
    # Flags from <linux/tun_if.h>
    IFF_TAP = 0x0002
    IFF_NO_PI = 0x1000
    TUNSETIFF = 0x400454ca
    TUNSETOWNER = 0x400454cc

    tun = os.open("/dev/net/tun", os.O_RDWR)
    ifr_name = iface.encode() + b'\x00'*(16-len(iface.encode()))
    ifr = struct.pack("16sH22s", ifr_name, IFF_TAP | IFF_NO_PI, b'\x00'*22)
    ret = fcntl.ioctl(tun, TUNSETIFF, ifr)

    subprocess.check_call(f"ip link set {iface} up", shell=True)
    # Have to set an IP address for the tap. Since I'm only running
    # this at home, ...1.50 likely ain't being used.
    subprocess.check_call(f"ip addr add 192.168.1.50/24 dev {iface}", shell=True)
    return tun

def del_tun(tun):
    os.close(tun)

def read_tun(tun):
    return os.read(tun, 1518)

def write_tun(tun, data):
    return os.write(tun, data)

def read_pkts(tun, count):
    pkts = []
    for i in range(count):
        pkts.append(read_tun(tun))
    return pkts

def watch_tun(tun):
    while True:
        pkt = read_tun(tun)
        print(e.EthernetFrame(pkt))


if __name__ == "__main__":
    tap = make_tun("tap0")
    code.interact(local=locals())
