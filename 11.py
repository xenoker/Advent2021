from puzzleinput import getlines
from itertools import permutations
from copy import deepcopy
DATA = [list(map(int,line)) for line in getlines(11)]
RLIM,CLIM = list(range(len(DATA))), list(range(len(DATA[0])))
DIR = list(permutations((-1,0,1),2)) + [(1,1),(-1,-1)]

def flash(r,c,data,flashed):
    data[r][c] = 0
    flashed.append((r,c))
    for dr,dc in DIR:
        if r+dr not in RLIM or c+dc not in CLIM: continue
        if (r+dr,c+dc) in flashed: continue
        if data[r+dr][c+dc] < 9: data[r+dr][c+dc] += 1
        else: flash(r+dr,c+dc,data,flashed)

def step(data):
    flashed = []
    for r,row in enumerate(data):
        for c,d in enumerate(row):
            if (r,c) in flashed: continue
            if data[r][c] < 9: data[r][c] += 1
            else: flash(r,c,data,flashed)
    return len(flashed)

def part1():
    data = deepcopy(DATA)
    return sum(step(data) for x in range(100))
def part2():
    data = deepcopy(DATA)
    return next((s for s in range(1,1000000) if step(data)==100))

if __name__ == '__main__':
    assert part1()==1665
    assert part2()==235




    
    

