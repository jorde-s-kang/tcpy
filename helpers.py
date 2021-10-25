import EthernetFrame as e
import os

def pkt_from_file(fname):
    with open(fname) as f:
        return e.EthernetFrame(bytes.fromhex(f.readline()))
