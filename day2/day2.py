# Reading the input file:

f = open('input.txt', 'r')
input_ml = f.read()

exemplo = """A Y
B X
C Z"""

shapes = {'X': 1, 'Y': 2, 'Z': 3}

def scoring_1(data):
    score = 0

    for x in data:
        for shape in shapes.keys():
            if x[2] == shape:
                score += shapes[shape]
        if x[0] == 'A':
            if x[2] == 'X': # draw
                score += 3
            elif x[2] == 'Y': # win
                score += 6
        elif x[0] == 'B':
            if x[2] == 'Y': # draw
                score += 3
            elif x[2] == 'Z': # win
                score += 6
        elif x[0] == 'C':
            if x[2] == 'Z': # draw
                score += 3
            elif x[2] == 'X': # win
                score += 6
    return score


win_lose = {'X': 0, 'Y': 3, 'Z': 6}


def scoring_2(data):
    score = 0

    for x in data:        
        if x[0] == 'A': # elf chose rock
            if x[2] == 'X': # lose #escolher scissors
                score += 3
            elif x[2] == 'Y': # draw # escolher rock
                score += 3 + 1
            elif x[2] == 'Z': # win #escolher papel
                score += 6 + 2
        elif x[0] == 'B': #elf chose paper
            if x[2] == 'X': # lose #escolher rock
                score += 1
            elif x[2] == 'Y': # draw # escolher paper
                score += 3 + 2
            elif x[2] == 'Z': # win #escolher scissors
                score += 6 + 3
        elif x[0] == 'C': # elf chose scissors
            if x[2] == 'X': # lose #escolher paper
                score += 2
            elif x[2] == 'Y': # draw # escolher scissors
                score += 3 + 3
            elif x[2] == 'Z': # win #escolher rock
                score += 6 + 1
    return score


data = input_ml.splitlines()
# data = exemplo.splitline()

print(f'Solution part 1: {scoring_1(data)}')
print(f'Solution part 2: {scoring_2(data)}')