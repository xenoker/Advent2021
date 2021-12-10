from puzzleinput import getlines
LINES = getlines(10)
PAIRS = dict(('()','[]','<>','{}'))
SCORING1 = {')':3,']':57,'}':1197,'>':25137}
SCORING2 = {')':1,']':2,'}':3,'>':4}

def parts():
    score1, scores2 = 0, []
    for line in LINES:
        stack = []
        for c in line:
            if c in PAIRS:
                stack.append(c)
            elif c != PAIRS[stack.pop()]:
                score1 += SCORING1[c]
                break
        else:
            score2 = 0
            for c in reversed(stack):
                score2 = score2 *5 + SCORING2[PAIRS[c]]
            scores2.append(score2)
    scores2.sort()
    return score1, scores2[len(scores2)//2]

if __name__ == '__main__':
    assert parts()==(392139,4001832844)



    
    

