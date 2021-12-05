from puzzleinput import getlines
LINES = getlines(5)

def getpoints(ln,part2):
    ln = ln.replace(' -> ',',')
    Ax,Ay,Bx,By = map(int,ln.split(','))
    if Ax==Bx: return ((Ax,y) for y in range(min(Ay,By),max(Ay,By)+1))
    elif Ay==By: return ((x,By) for x in range(min(Ax,Bx),max(Ax,Bx)+1))
    elif not part2: return []
    sx,sy = Bx>Ax and 1 or -1, By>Ay and 1 or -1
    return ((Ax+r*sx,Ay+r*sy) for r in range(max(Ax,Bx)-min(Ax,Bx)+1))

def part(partnum):
    points = {}
    for line in LINES:
        for point in getpoints(line,partnum==2):
            points[point] = points.get(point,0) + 1
    return sum(1 for count in points.values() if count>1)
        
if __name__ == '__main__':
    assert part(1)==7380
    assert part(2)==21373

    
    

