def part1(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if(len(line) == 0):
            continue
        pair = line.split(',')
        pair1 = pair[0].split('-')
        pair2 = pair[1].split('-')
        if(int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])):
            total += 1
        elif(int(pair2[0]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1])):
            total += 1
    print(total)

def part2(lines):
    total = 0
    for line in lines:
        line = line.strip()
        if(len(line) == 0):
            continue
        pair = line.split(',')
        pair1 = pair[0].split('-')
        pair2 = pair[1].split('-')
        if(int(pair1[0]) >= int(pair2[0]) and int(pair1[0]) <= int(pair2[1])):
            total += 1
        elif(int(pair1[1]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1])):
            total += 1
        elif(int(pair2[0]) >= int(pair1[0]) and int(pair2[0]) <= int(pair1[1])):
            total += 1
        elif(int(pair2[1]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1])):
            total += 1
    print(total)


with open('day4.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)