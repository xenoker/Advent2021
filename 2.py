from puzzleinput import getlines
LINES = getlines(2)

class Submarine:
    def __init__(self):
        self.D,self.F,self.A=0,0,0
    def run(self):
        for line in LINES:
            d,v = line.split()
            getattr(self,d)(int(v))
        return self.D*self.F

class part1(Submarine):
    def forward(self,v): self.F += v
    def up(self,v): self.D -= v
    def down(self,v): self.D += v

class part2(Submarine):
    def forward(self,v):
        self.F += v
        self.D += self.A*v
    def up(self,v): self.A -= v
    def down(self,v): self.A += v

if __name__ == '__main__':
    assert part1().run()==1604850
    assert part2().run()==1685186100

