# Set head and tail global variables to centre
#        x    Y
head = [500, 500]
tail = [500, 500]
# allocate 1000 * 1000 matrix and put start in centre
matrix = [[0]*1000 for i in range(1000)] 
matrix[500][500] = '#'
# second global matrix for part 2
matrix2 = [[0]*1000 for i in range(1000)]
matrix2[500][500] = '#'
def part1(lines):
    tail_count = 1
    for line in lines:
        split_line = line.split(' ')
        direction = split_line[0]
        count = split_line[1].strip()
        count = int(count)
        tail_count += handle_movement1(direction, count)
    print(tail_count)

def handle_movement1(direction, count):
    tail_new_square = 0
    if direction == 'U':
        for i in range(count):
            head[1] -= 1
            tail_new_square += check_tail()
    if direction == 'R':
        for i in range(count):
            head[0] += 1
            tail_new_square += check_tail()
    if direction == 'D':
        for i in range(count):
            head[1] += 1
            tail_new_square += check_tail()
    if direction == 'L':
        for i in range(count):
            head[0] -= 1
            tail_new_square += check_tail()
    return tail_new_square

def check_tail():
    new_square = 0
    sign = lambda x: 0 if not x else int(x/abs(x))

    if (abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1):
        return new_square

    # move tail diagonal
    if (abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1) and (tail[1] != head[1] and tail[0] != head[0]):
        y = sign(head[1] - tail[1])*1
        x = sign(head[0] - tail[0])*1
        new_square = change_position(y, x, tail)
    # move horizontal or vertical
    else:
        if (head[0] == tail[0]):
            y = sign(head[1] - tail[1])*1
            new_square = change_position(y, 0, tail)
        if (head[1] == tail[1]):
            x = sign(head[0] - tail[0])*1
            new_square = change_position(0, x, tail)
    return new_square

def change_position(y, x, tail):
    tail[1] += y
    tail[0] += x
    if matrix[tail[1]][tail[0]] != '#':
        matrix[tail[1]][tail[0]] = '#'
        return 1
    return 0


def part2(lines):
    # create array of size 10, index 0 will be head and index 1-9 will be tail elements
    tail_matrix = [[500, 500] for i in range(10)] 
    tail_count = 1
    for line in lines:
        split_line = line.split(' ')
        direction = split_line[0]
        count = split_line[1].strip()
        count = int(count)
        tail_count += handle_movement2(direction, count, tail_matrix)
    print(tail_count)

def handle_movement2(direction, count, tail_matrix,):
    tail_new_square = 0
    if direction == 'U':
        for i in range(count):
            tail_matrix[0][1] -= 1
            tail_new_square += check_tail2_start(tail_matrix)
    if direction == 'R':
        for i in range(count):
            tail_matrix[0][0] += 1
            tail_new_square += check_tail2_start(tail_matrix)
    if direction == 'D':
        for i in range(count):
            tail_matrix[0][1] += 1
            tail_new_square += check_tail2_start(tail_matrix)
    if direction == 'L':
        for i in range(count):
            tail_matrix[0][0] -= 1
            tail_new_square += check_tail2_start(tail_matrix)
    return tail_new_square

def check_tail2_start(tail_matrix):
    result = 0
    for i in range(1, 10):
        if check_tail2(tail_matrix, i):
            result = 1
    return result
    

def check_tail2(tail_matrix, index):
    # tail_matrix[index] is current tail
    # tail_matrix[index - 1] is current head
    new_square = False
    head_y_pos = tail_matrix[index-1][1]
    head_x_pos = tail_matrix[index-1][0]
    tail_y_pos = tail_matrix[index][1]
    tail_x_pos = tail_matrix[index][0]
    sign = lambda x: 0 if not x else int(x/abs(x))

    if (abs(head_y_pos - tail_y_pos) <= 1 and abs(head_x_pos - tail_x_pos) <= 1):
        return new_square

    # move tail diagonal
    if (abs(head_x_pos - tail_x_pos) > 1 or abs(head_y_pos - tail_y_pos) > 1) and (tail_y_pos != head_y_pos and tail_x_pos != head_x_pos):
        y = sign(head_y_pos - tail_y_pos)*1
        x = sign(head_x_pos - tail_x_pos)*1
        new_square = change_position2(y, x, index, tail_matrix)
    # move horizontal or vertical
    else:
        if (head_x_pos == tail_x_pos):
            y = sign(head_y_pos - tail_y_pos)*1
            new_square = change_position2(y, 0, index, tail_matrix)
        if (head_y_pos == tail_y_pos):
            x = sign(head_x_pos - tail_x_pos)*1
            new_square = change_position2(0, x, index, tail_matrix)
    
    return new_square

def change_position2(y, x, index, tail_matrix):
    tail_matrix[index][1] += y
    tail_matrix[index][0] += x
    if matrix2[tail_matrix[index][1]][tail_matrix[index][0]] != '#' and index == 9:
        matrix2[tail_matrix[index][1]][tail_matrix[index][0]] = '#'
        return True
    return False
    
with open('day9.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)