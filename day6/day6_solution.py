def part1(line):
    character_num = 0
    for i in range(0, len(line)):
        start_packet = []
        for j in range(0, 4):
            start_packet.insert(0, line[i+j])
        packet_set = set(start_packet)
        if(len(packet_set) == 4):
            character_num = i + 4
            break
    print(character_num)


def part2(lines):
    character_num = 0
    for i in range(0, len(line)):
        start_packet = []
        for j in range(0, 14):
            start_packet.insert(0, line[i+j])
        packet_set = set(start_packet)
        if(len(packet_set) == 14):
            character_num = i + 14
            break
    print(character_num)


with open('day6.txt') as f:
    line = f.readline()
part1(line)
part2(line)