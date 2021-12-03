from puzzleinput import getlines
LINES = getlines(3)
LEN = len(LINES[0])

def common(L,pos,com=1):
    psum =  sum(int(l[pos]) for l in L)
    half = len(L)/2
    if psum == half: return com
    if com: return psum > half
    return psum < half

def part1():
    G,E = 0,0
    for n in range(LEN):
        com = common(LINES,-1-n)
        G += com*(2**n)
        E += (not com)*(2**n)
    return G*E

def reduce(val):
    L = LINES.copy()
    for n in range(LEN):
        com = common(L,n,val)
        L = [l for l in L if int(l[n])==com]
        if len(L) == 1: return L[0]

def part2():
    O = reduce(True)
    C = reduce(False)
    return int(O,2)*int(C,2)

if __name__ == '__main__':
    assert part1()==1540244
    assert part2()==4203981

    
    

