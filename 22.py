from puzzleinput import getlines
from collections import Counter
from functools import reduce

def linetolist(line):
    state, xyz = line.split()
    return (state=='on' and 1 or -1, tuple(tuple(map(int,a[2:].split('..'))) for a in xyz.split(','))) 

class Volume:
    def __init__(self):
        self.areas = Counter()
        
    def delta(self, sign, xyz):
        for area,c in self.overlaps(xyz):
            self.areas[area] -= c
        if sign>0: self.areas[xyz] += sign

    def overlaps(self, xyz):
        out = []
        for area, c in self.areas.items():
            o = []
            for i in range(3):
                a1, a2 = area[i]
                b1, b2 = xyz[i]
                o1, o2 = max(a1,b1), min(a2,b2)
                if o1 > o2: break
                o.append((o1, o2))
            else: out.append((tuple(o), c))
        return out

    @property
    def on(self):
        return sum(c*reduce(lambda a,b:a*b,[j-i+1 for i,j in l]) for l,c in self.areas.items())


def part(part2=False):
    V = Volume()
    for line in getlines(22):
        sign, xyz = linetolist(line)
        if not part2 and abs(xyz[0][0])>50: break
        V.delta(sign, xyz)
    return V.on

if __name__ == '__main__':
    assert part() == 570915
    assert part(2) == 1268313839428137


