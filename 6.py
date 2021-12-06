from puzzleinput import get
FISH = get(6).split(',')

def nextday(D):
    D2 = dict((k-1,d) for k,d in D.items())
    if -1 in D2:
        c = D2.pop(-1)
        D2[8], D2[6] = c, c+D2.get(6,0) 
    return D2

def part(days):
    D = dict((int(x),FISH.count(x)) for x in set(FISH))
    for day in range(days): D = nextday(D)
    return sum(d for d in D.values())
        
if __name__ == '__main__':
    assert part(80)==351092
    assert part(256)==1595330616005


    
    

