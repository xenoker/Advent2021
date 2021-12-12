from puzzleinput import getlines

LINKS = dict()
for line in getlines(12):
    a,b = line.split('-')
    LINKS[a] = LINKS.get(a,[])+[b]
    LINKS[b] = LINKS.get(b,[])+[a]    

def move(path, out, special=''):
    if path[-1] == 'end':
        out.append(tuple(path))
        return
    for link in LINKS[path[-1]]:
        if link in path and link.islower() and link != special: continue
        if link==special and path.count(special) == 2: continue
        move(path+[link],out,special)   

def part1():
    paths = []
    move(['start'],paths)
    return len(paths)

def part2():
    paths = []
    for small in [l for l in LINKS.keys() if l.islower() and l not in ['start','end']]:
        move(['start'],paths,small)
    return len(set(paths))

if __name__ == '__main__':
    assert part1()==5076
    assert part2()==145643




    
    

