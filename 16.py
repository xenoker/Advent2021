from puzzleinput import get
from math import prod
TEXT = get(16)

class BITS:
    def __init__(self, hexstr):
        self.NUM = int(hexstr,16)
        self.BINS = f'{self.NUM:b}'
        if len(self.BINS)%8:
            self.BINS = self.BINS.zfill((len(self.BINS)//8+1)*8)
        self.P = 0
        self.L = []
        self.vsum = 0
        self.parse()
        
    def read(self, n, asint=True):
        out = self.BINS[self.P:self.P+n]
        self.P += n
        if asint: return int(out,2)
        return out
    
    def readheader(self):
        V = self.read(3)
        self.vsum += V
        T = self.read(3)
        return V,T
    
    def readliteral(self, V, T):
        G = []
        while True:
            B = self.read(5,False)
            G.append(B[1:])
            if B[0] != '1': break
        N = int(''.join(G),2)
        return (V, T, N)
    
    def readoperator(self, V, T):
        ltid = self.read(1)
        if ltid:
            nsp = self.read(11)
            opL = []
            for p in range(nsp):
                self.readnext(opL)
            return (V, T, opL)
        else:
            bsp = self.read(15)
            end = self.P + bsp
            opL = []
            while self.P < end:
                self.readnext(opL)
            return (V, T, opL)
        
    def readnext(self, subL=None):
        V, T = self.readheader()
        if T == 4: p = self.readliteral(V, T)
        else: p = self.readoperator(V, T)
        if subL == None: self.L.append(p)
        else: subL.append(p)
        
    def parse(self):
        while self.P < len(self.BINS)-8:
            self.readnext()
            
    @property
    def eval(self):
        assert len(self.L)==1
        return self.evalone(self.L[0])
    
    def evalone(self,pkt):
        V, T, X = pkt
        if T==0: return sum(self.evalone(p) for p in X)
        if T==1: return prod(self.evalone(p) for p in X)
        if T==2: return min(self.evalone(p) for p in X)
        if T==3: return max(self.evalone(p) for p in X)
        if T==4: return X
        if T in [5,6,7]: assert len(X)==2
        if T==5: return self.evalone(X[0]) > self.evalone(X[1])
        if T==6: return self.evalone(X[0]) < self.evalone(X[1])
        if T==7: return self.evalone(X[0]) == self.evalone(X[1])


def part1(): return BITS(TEXT).vsum
def part2(): return BITS(TEXT).eval

if __name__ == '__main__':
    assert part1() == 979
    assert part2() == 277110354175

    VSUMTESTS = {'8A004A801A8002F478':16,
                 '620080001611562C8802118E34':12,
                 'C0015000016115A2E0802F182340':23,
                 'A0016C880162017C3686B18A3D4780':31}
    for h,s in VSUMTESTS.items():
        assert BITS(h).vsum==s
        
    assert BITS('9C0141080250320F1802104A08').L == [(4, 7, [(2, 0, [(2, 4, 1), (4, 4, 3)]), (6, 1, [(0, 4, 2), (2, 4, 2)])])]

    EVALTESTS = {'C200B40A82':3,
                 '04005AC33890':54,
                 '880086C3E88112':7,
                 'CE00C43D881120':9,
                 'D8005AC2A8F0':1,
                 'F600BC2D8F':0,
                 '9C005AC2F8F0':0,
                 '9C0141080250320F1802104A08':1}
    for h,s in EVALTESTS.items():
        assert BITS(h).eval==s




    
    

