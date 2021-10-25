import code
import tap
import helpers as h

arp_table = {}


class ARPPacket:
    def __init__(self, data):
        self.htype = data[:2]
        self.ptype = data[2:4]
        self.hlen  = data[4]
        self.plen  = data[5]
        self.op    = data[6:8]
        self.sha   = data[8:14]
        self.spa   = data[14:18]
        self.tha   = data[18:24]
        self.tpa   = data[24:30]
        self.raw = data

    def __str__(self):
        return self.raw.hex()    
        
    


if __name__ == "__main__":
    e = h.pkt_from_file("arp.txt")
    # print(e)
    # code.interact(local=locals())
