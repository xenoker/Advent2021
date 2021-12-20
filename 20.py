from puzzleinput import getlines
from collections import defaultdict
LINES = getlines(20)
CB = {'.':False,'#':True}
ENH = [CB[x] for x in LINES[0]]
LOOP = list((dr,dc) for dr in [1,0,-1] for dc in [1,0,-1])
INPUT = defaultdict(bool)
for r,row in enumerate(LINES[1:]):
    for c,d in enumerate(row):
        INPUT[(r,c)] = CB[d]

def step(d,default):
    dout = defaultdict(bool)
    S = set(d.keys())
    while S:
        r,c = S.pop()
        i,b = 0,0
        for i,delta in enumerate(LOOP):
            dr,dc = delta
            xy = (r+dr,c+dc)
            if (r,c) in d and xy not in dout: S.add(xy)
            if (xy in d and d[xy]) or (xy not in d and default):
                b += 2**i
        dout[(r,c)] = ENH[b]
    return dout

def part(n):
    D = INPUT.copy()
    for i in range(n):
        D = step(D, i%2!=0)
    return sum(1 for x in D.values() if x)

if __name__ == '__main__':
    assert part(2) == 5461
    assert part(50) == 18226 
  

