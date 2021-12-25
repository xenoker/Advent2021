from puzzleinput import getlines
LINES = getlines(25)
MAXR,MAXC = len(LINES), len(LINES[0])
DATA = dict(((r,c),it) for r,row in enumerate(LINES) for c,it in enumerate(row) if it in 'v>' )

def move(D):
    moved = False
    DC = D.copy()
    for p,d in DC.items():
        if d!='>': continue
        r,c = p
        if (r,(c+1)%MAXC) not in DC:
            D[r,(c+1)%MAXC] = D.pop((r,c))
            moved = True
    DC = D.copy()
    for p,d in DC.items():
        if d!='v': continue
        r,c = p
        if ((r+1)%MAXR,c) not in DC:
            D[(r+1)%MAXR,c] = D.pop((r,c))
            moved = True
    return moved

def part1():
    for x in range(1,1000):
        if not move(DATA): return x

if __name__ == '__main__':
    assert part1() == 374



