from math import ceil
from json import loads
from copy import deepcopy
from functools import reduce
from puzzleinput import getlines
LIST = [loads(x) for x in getlines(18)]

def magnitude(exp):
    if type(exp) == list:
        return 3*magnitude(exp[0]) + 2*magnitude(exp[1])
    return exp

def reduction(exp):
    cexp = deepcopy(exp)
    while 1:
        if not (maybeexplode(cexp) or maybesplit(cexp)): return cexp

def maybeexplode(exp, back=[]): #the worst function ever to debug
    if type(exp) == int: return False
    if len(back) < 4: return maybeexplode(exp[0], back+[(exp,0)]) or maybeexplode(exp[1], back+[(exp,1)])
    for side in [0,1]:
        for (e, s) in back[::-1]:
            if s == side:
                if type(e[not side]) == int:
                    e[not side] += exp[not side]
                    break
                else:
                    e = e[not side]
                    while type(e[side]) != int:
                        e = e[side]
                    e[side] += exp[not side]
                    break
    e, s = back[-1]
    e[s] = 0
    return True

def maybesplit(exp, back=[]):
    if type(exp) == list:
        return maybesplit(exp[0], back+[(exp, 0)]) or maybesplit(exp[1], back+[(exp, 1)])
    if exp < 10: return False
    e, s = back[-1]
    e[s] = [exp//2, ceil(exp/2)]
    return True

def part1():
    return magnitude(reduce(lambda x,y:reduction([x,y]),LIST))
def part2():
    return max(magnitude(reduction([x,y])) for x in LIST for y in LIST if x!=y )

if __name__ == '__main__':
    assert part1() == 4072
    assert part2() == 4483

    
    

