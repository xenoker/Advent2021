TX, TY = list(range(155,182+1)),list(range(-117,-67+1))

def fire(Vx, Vy, maxH):
    x,y,H = 0,0,0
    while 1:
        if Vx==0 and x not in TX: return False
        if y<min(TY): return False
        if Vy==0 and y>0: H = y
        if x in TX and y in TY:
            if H: maxH.append(H)
            return True
        x += Vx
        y += Vy
        if Vx>0: Vx -=1
        Vy -= 1
    
def part():
    maxH, hits = [], 0
    for y in range(min(TY), max(TX)):
        for x in range(1, max(TX)*2):
            hits += fire(x, y, maxH)
    return max(maxH), hits

if __name__ == '__main__':
    assert part() == (6786, 2313)




    
    

