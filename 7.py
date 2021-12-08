from puzzleinput import get
from functools import lru_cache
CRABS = list(map(int,get(7).split(',')))
s_crabs = set(CRABS)
c_crabs = dict((k,CRABS.count(k)) for k in s_crabs)

@lru_cache(maxsize = len(c_crabs)*2)
def fuelcost(pn,diff):
    if pn==1: return diff
    return sum(range(1,diff+1))

def part(pn):
    return min( sum(fuelcost(pn,abs(p-pos))*n for p,n in c_crabs.items()) for pos in range(min(s_crabs),max(s_crabs)) )

#def part(pn): return min( sum( pn==1 and abs(p-pos)*n or sum(range(1,abs(p-pos)+1))*n for p,n in c_crabs.items()) for pos in range(min(c_crabs),max(c_crabs)) )

if __name__ == '__main__':
    assert part(1)==349769
    assert part(2)==99540554


    
    

