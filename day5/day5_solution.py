def part1(lines):
    get_creates = True
    crate_spaces = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    crate_yard = []
    crate_yard = [ [] for _ in range(9)]
    for line in lines:
        if(len(line.strip()) < 1):
            continue
        if(line[1] == '1'):
            get_creates = False
            for list in crate_yard:
                list.reverse()
            continue
        if get_creates:
            for i in crate_spaces:
                if(line[i] != ' '):
                    crate_yard[crate_spaces.index(i)].insert(0, line[i])
            continue

        parse_line = line.split(' ')
        amount = int(parse_line[1])
        source = int(parse_line[3]) - 1
        destination = int(parse_line[5]) - 1

        for i in range(0, amount):
            crate_yard[destination].insert(0, crate_yard[source].pop(0))
    # print top crates
    for list in crate_yard:
        print(list[0], end='')

def part2(lines):
    get_creates = True
    crate_spaces = [1, 5, 9, 13, 17, 21, 25, 29, 33]
    crate_yard = []
    crate_yard = [ [] for _ in range(9)]
    for line in lines:
        if(len(line.strip()) < 1):
            continue
        if(line[1] == '1'):
            get_creates = False
            for list in crate_yard:
                list.reverse()
            continue
        if get_creates:
            for i in crate_spaces:
                if(line[i] != ' '):
                    crate_yard[crate_spaces.index(i)].insert(0, line[i])
            continue
        parse_line = line.split(' ')
        amount = int(parse_line[1])
        source = int(parse_line[3]) - 1
        destination = int(parse_line[5]) - 1

        temp_list = []
        for i in range(0, amount):
            temp_list.insert(0, crate_yard[source].pop(0))
        temp_list.reverse()
        temp_list.extend(crate_yard[destination])
        crate_yard[destination] = temp_list
    # Print first element in each list
    for list in crate_yard:
        print(list[0], end='')



with open('day5.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)