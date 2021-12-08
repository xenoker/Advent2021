from puzzleinput import getlines
LINES = [tuple(map(lambda x:x.split(),line.split(' | '))) for line in getlines(8)]

def part1():
    return sum(sum(1 for z in y if len(z) in [2,3,4,7]) for x,y in LINES)

def getleng(L,leng):
    return [l for l in L if len(l)==leng]
def untangle(wire):
    wire = list(map(set,wire))
    D = dict()
    for a,b in [(1,2),(4,4),(7,3),(8,7)]: # 1,4,7,8
        D[a] = getleng(wire,b)[0] 
    for x in getleng(wire,6): #0,6,9
        if D[4].issubset(x): D[9] = x
        elif D[1].issubset(x): D[0] = x
        else: D[6] = x
    for x in getleng(wire,5): # 2,3,5
        if x.issubset(D[6]): D[5] = x
        elif D[1].issubset(x): D[3] = x
        else: D[2] = x
    return dict((''.join(sorted(d)),k) for k,d in D.items())
def decode(wire,digits):
    D = untangle(wire)
    return sum(D[''.join(sorted(digit))]*(10**n) for n,digit in enumerate(reversed(digits)) )
def part2():
    return sum(decode(*line) for line in LINES)
    

if __name__ == '__main__':
    assert part1()==416
    assert part2()==1043697


    
    

