from puzzleinput import getints
INTS = getints(1)

def part1():
    return sum(b>a for a,b in zip(INTS,INTS[1:]))
#def part2():
#    return sum(sum(INTS[i+1:][:3])>sum(INTS[i:][:3]) for i in range(len(INTS)-3))
def part2():
    return sum(b>a for a,b in zip(INTS,INTS[3:]))

if __name__ == '__main__':
    assert part1()==1342
    assert part2()==1378

