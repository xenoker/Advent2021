from puzzleinput import getlines
from collections import Counter
DATA = getlines(14)
TEXT = DATA[0]
SUBS = dict()
for line in DATA[1:]:
    a, b = line.split(' -> ')
    SUBS[tuple(a)] = b

def part(steps):
    paircounts = Counter(zip(TEXT, TEXT[1:]))
    singlecounts = Counter(TEXT)
    for step in range(steps):
        delta = Counter()
        for pair, ins in SUBS.items():
            if pair in paircounts:
                num = paircounts[pair]
                delta[pair] -= num
                delta[(pair[0], ins)] += num
                delta[(ins, pair[1])] += num
                singlecounts[ins] += num
        paircounts += delta
    return max(singlecounts.values()) - min(singlecounts.values())

if __name__ == '__main__':
    assert part(10)==2360
    assert part(40)==2967977072188



    
    

