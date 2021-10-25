import sys
import helpers as h
import code
from arp import ARPPacket


class EthernetFrame:
    def __init__(self, pkt):
        self.dest    = pkt[:6]
        self.src     = pkt[6:12]
        self.ptype   = pkt[12:14]
        self.raw     = pkt
        payload = pkt[14:]
        ptype = self.get_ethertype(self.ptype)
        if type(ptype) == type:
            self.payload = ptype(payload)
        else:
            self.payload = payload

    def __str__(self):
        src = self.decode_mac(self.src)
        dest = self.decode_mac(self.dest)
        pl = None
        if type(self.payload) == bytes:
            pl = self.payload.hex()
        else:
            pl = str(self.payload)
        return f"{src} -> {dest} (type: {self.get_ethertype(self.ptype)}) payload: {self.payload}"

    def decode_mac(self, raw):
        hexmac = raw.hex()
        l = [hexmac[i:i+2] for i in range(0, len(hexmac), 2)]
        return ":".join(l)

    def get_ethertype(self, key):
        types = {"0800": "IPv4",
                 "86DD": "IPv6",
                 "0806": ARPPacket}
        try:
            return types[key.hex().upper()]
        except KeyError:
            return key.hex().upper()

if __name__ == "__main__":
    e = h.pkt_from_file("test_pkt.txt")
    print(e)
    code.interact(local=locals())
