from puzzleinput import getlines
LINES = getlines(4)
CALL = LINES.pop(0).split(',')

class BingoCard:
    def __init__(self,rows):
        self.nums = [row.split() for row in rows]
        self.marked = [[False]*5 for x in range(5)]
        self.won = False
    def mark(self,number):
        for r,row in enumerate(self.nums):
            for c,num in enumerate(row):
                if num == number: self.marked[r][c] = True
        return self.check()
    def check(self):
        if any(sum(row)==5 for row in self.marked): return True
        if any(sum(row[n] for row in self.marked)==5 for n in range(5) ): return True
    def score(self,last):
        return int(last) * sum(int(num) for r,row in enumerate(self.nums) for c,num in enumerate(row) if not self.marked[r][c])
                
def makecards():
    return [BingoCard(LINES[x:x+5]) for x in range(0,len(LINES),5)]

def part1():
    cards = makecards()
    for n in CALL:
        for card in cards:
            if card.mark(n):
                return card.score(n)

def part2():
    wins = 0
    cards = makecards()
    for n in CALL:
        for card in cards:
            if not card.won and card.mark(n):
                wins += 1
                card.won = True
                if wins == len(cards):
                    return card.score(n)

if __name__ == '__main__':
    assert part1()==8136
    assert part2()==12738

    
    

