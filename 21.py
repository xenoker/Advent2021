from itertools import cycle, product
from functools import lru_cache

P1, P2 = 7, 9


DICE = cycle(range(1, 101))
def game1(p1, p2, s1=0, s2=0, dr=0):
    if s1 >= 1000 or s2 >= 1000: return dr*min(s1,s2)
    roll = sum(next(DICE) for _ in range(3))
    pt = (p1 + roll) % 10
    return game1(p2, pt, s2, s1 + pt+1, dr+3)

def part1():
    return game1(P1-1, P2-1)


ROLLS = list(sum(x) for x in product([1,2,3], [1,2,3], [1,2,3]))
@lru_cache(maxsize=100000)
def game2(p1, p2, s1=0, s2=0):
    if s1 >= 21: return (1, 0)
    if s2 >= 21: return (0, 1)
    w1, w2 = 0,0
    for r in ROLLS:
        pt = (p1 + r) % 10
        dw2, dw1 = game2(p2, pt, s2, s1 + pt+1)
        w1 += dw1
        w2 += dw2
    return (w1,w2)

def part2():
    return max(game2(P1-1, P2-1))


if __name__ == '__main__':
    assert part1() == 679329
    assert part2() == 433315766324816
