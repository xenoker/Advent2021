from puzzleinput import getlines
DATA = getlines(13)
POINTS = [tuple(map(int,line.split(',')))for line in DATA if ',' in line]
FOLDS = [line[11:].split('=') for line in DATA if line.startswith('fold')]

def fold(L, d, n):
    out = set()
    for x,y in L:
        if d=='x' and x==n or d=='y' and y==n: continue #all fold lines seeem to be empty anyway
        if d=='x' and x>n: out.add((n-(x-n),y))
        elif d=='y' and y>n: out.add((x,n-(y-n)))
        else: out.add((x,y))
    return out

def part1():
    d, n = FOLDS[0]
    return len(fold(POINTS, d, int(n)))

def part2():
    L = POINTS.copy()
    for d,n in FOLDS: L = fold(L, d, int(n))
    mx, my = max(x for x,y in L), max(y for x,y in L)
    return '\n'.join(''.join((x,y) in L and '#' or ' ' for x in range(mx+1)) for y in range(my+1))

if __name__ == '__main__':
    assert part1()==664
    print(part2()) #prints EFJKZLBL




    
    

