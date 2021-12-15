from puzzleinput import getlines
from heapq import heapify, heappop, heappush
from collections import defaultdict
DATA = [list(map(int,line)) for line in getlines(15)]
SIZE = len(DATA)
DIR = [(1,0),(0,1),(-1,0),(0,-1)]
START = (0,0)

def getdata(r,c,partnum):
    if partnum == 1: return DATA[r][c]
    num = DATA[r%SIZE][c%SIZE]+ (r//SIZE) + (c//SIZE)
    if num > 9: return num%9
    return num

def part(partnum):
    LIM = list(range(len(DATA)*(partnum==1 or 5)))
    END = (LIM[-1], LIM[-1])
    Q = [(0, START)]
    heapify(Q)
    RISK = defaultdict(lambda:999999)
    while Q:
        risk, point = heappop(Q)
        r, c = point
        for dr,dc in DIR:
            r2, c2 = r+dr, c+dc
            if r2 not in LIM or c2 not in LIM: continue
            datapoint = getdata(r2,c2,partnum)
            if risk + datapoint < RISK[(r2, c2)]:
                RISK[(r2, c2)] = risk + datapoint
                heappush(Q, (risk + datapoint, (r2, c2)))
    return RISK[END]

if __name__ == '__main__':
    assert part(1)==373
    assert part(2)==2868




    
    

