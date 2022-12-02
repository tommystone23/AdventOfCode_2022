# Part 1
def part1(lines):
    cur_max = 0
    cur_num = 0
    for line in lines:
        if(len(line.strip()) == 0):
            if(cur_num > cur_max):
                cur_max = cur_num
                cur_num = 0
                continue
            cur_num = 0
            continue
        cur_num += int(line.strip())
    print(cur_max)

# Part 2
def part2(lines):
    cur_num = 0
    top_3 = [0, 0, 0]
    for line in lines:
        if(len(line.strip()) == 0):
            count = 0
            for value in top_3:
                if(cur_num > value):
                    top_3.insert(count, cur_num)
                    break
                count += 1
            while(len(top_3) > 3):
                top_3.pop(len(top_3) - 1)
            cur_num = 0
            continue
        cur_num += int(line.strip())
    max = 0
    for value in top_3:
        max += value
    print(max)

with open('day1.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)