def get(i):
    with open(f'./inputs/{i}.txt') as f:
        return f.read()
def getlines(i):
    with open(f'./inputs/{i}.txt') as f:
        return [x for x in f.read().split('\n') if x]
def getints(i):
    with open(f'./inputs/{i}.txt') as f:
        return [int(x) for x in f.read().split('\n') if x]
