def part1(lines):
    win = {'A Y':8, 'B Z':9, 'C X':7}
    loss = {'A Z':3, 'B X':1, 'C Y':2}
    draw = {'A X':4, 'B Y':5, 'C Z':6}
    total_score = 0
    for line in lines:
        result = line.strip()
        if(len(result) == 0):
            continue
        if(result in win):
            total_score += win[result]
        elif(result in loss):
            total_score += loss[result]
        else:
            total_score += draw[result]
    print(total_score)

def part2(lines):
    opponent_choice = ''
    outcome = ''
    total_score = 0
    win = {'A Y':8, 'B Z':9, 'C X':7}
    loss = {'A Z':3, 'B X':1, 'C Y':2}
    draw = {'A X':4, 'B Y':5, 'C Z':6}
    for line in lines:
        line = line.strip()
        if(len(line) == 0):
            continue
        opponent_choice = line[0]
        outcome = line[2]
        # Loss
        if(outcome == 'X'):
            keys = loss.keys()
            for key in keys:
                if(key[0] == opponent_choice):
                    total_score += loss[key]
        # Draw
        if(outcome == 'Y'):
            keys = draw.keys()
            for key in keys:
                if(key[0] == opponent_choice):
                    total_score += draw[key]
        # Win
        if(outcome == 'Z'):
            keys = win.keys()
            for key in keys:
                if(key[0] == opponent_choice):
                    total_score += win[key]

    print(total_score)


with open('day2.txt') as f:
    lines = f.readlines()

part1(lines)
part2(lines)
