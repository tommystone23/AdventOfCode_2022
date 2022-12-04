def part1(lines):
    total = 0
    for line in lines:
        half = len(line)//2
        half1 = line[:half]
        half2 = line[half:]
        dict1 = {half1[i]:ord(half1[i]) for i in range(0, len(half1), 1)}
        dict2 = {half2[i]:ord(half2[i]) for i in range(0, len(half2), 1)}
        for key in dict1.keys():
            if(key in dict2):
                if(key >= 'a' and key <= 'z'):
                    total += (dict1[key] - 96)
                if(key >= 'A' and key <= 'Z'):
                    total += (dict1[key] - 38)
    print(total)

def part2(lines):
    count = 0
    total = 0
    cur_group = []
    for line in lines:
        cur_group.append(line)
        count += 1
        if(count % 3 == 0):
            dict1 = {cur_group[0][i]:ord(cur_group[0][i]) for i in range(0, len(cur_group[0]), 1)}
            dict2 = {cur_group[1][i]:ord(cur_group[1][i]) for i in range(0, len(cur_group[1]), 1)}   
            dict3 = {cur_group[2][i]:ord(cur_group[2][i]) for i in range(0, len(cur_group[2]), 1)} 
            for key in dict1.keys():
                if(key in dict2 and key in dict3):
                    if(key >= 'a' and key <= 'z'):
                        total += (dict1[key] - 96)
                    if(key >= 'A' and key <= 'Z'):
                        total += (dict1[key] - 38)
            cur_group = []
    print(total)


with open('day3.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)