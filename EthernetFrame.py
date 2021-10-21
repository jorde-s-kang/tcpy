import code

class EthernetFrame:
    def __init__(self, pkt):
        self.dest  = pkt[:6]
        self.src   = pkt[6:12]
        self.ptype = pkt[12:14]
        self.payload = pkt[14:]

    def __str__(self):
        src = self.decode_mac(self.src)
        dest = self.decode_mac(self.dest)
        return f"{src} -> {dest} (type: {self.ptype}) payload: {self.payload.hex()}"

    def decode_mac(self, raw):
        hexmac = raw.hex()
        l = [hexmac[i:i+2] for i in range(0, len(hexmac), 2)]
        return ":".join(l)

if __name__ == "__main__":
    with open("test_pkt.txt") as f:
        e = EthernetFrame(bytes.fromhex(f.readline()))
    print(e)
    code.interact(local=locals())    
