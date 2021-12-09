from puzzleinput import getlines
from functools import reduce
DATA = [list(map(int,line)) for line in getlines(9)]
RLIM,CLIM = list(range(len(DATA))), list(range(len(DATA[0])))
DIR = ((0,1),(1,0),(-1,0),(0,-1))

def getpoint(r,c):
    if r not in RLIM or c not in CLIM: return 9
    return DATA[r][c]

def islow(r,c):
    n = DATA[r][c]
    return all(n<getpoint(r+dr,c+dc) for dr,dc in DIR )

LOW = [(r,c) for r,row in enumerate(DATA) for c,num in enumerate(row) if islow(r,c)]

def spreadcount(r,c,L):
    if getpoint(r,c) == 9 or (r,c) in L: return
    L.append((r,c))
    for dr,dc in DIR: spreadcount(r+dr,c+dc,L)
    return L

def part1():
    return sum(DATA[r][c]+1 for r,c in LOW)

def part2():
    return reduce(lambda a,b:a*b, sorted(len(spreadcount(r,c,[])) for r,c in LOW)[-3:] )    

if __name__ == '__main__':
    assert part1()==572
    assert part2()==847044


    
    

