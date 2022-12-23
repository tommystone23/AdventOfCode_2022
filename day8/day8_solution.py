    
def part1(lines):
    # Width and height of matrix
    height = len(lines)
    width = len(lines[0].strip())

    matrix = [[0]*height for i in range(width)]
    # initial visible trees
    visible_trees = (height * 2) + (width * 2) - 4

    matrix = construct_matrix(matrix, lines)

    # Check visible trees
    # Start at index 1 and end length - 1 for width and height
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if check_visible(j, i, int(matrix[i][j]), matrix):
                visible_trees += 1
    print(visible_trees)

def construct_matrix(matrix, lines):
    for i in range(len(lines)):
        for j in range(len(lines[i].strip())):
            matrix[i][j] = lines[i][j].strip()
    return matrix

def check_visible(xPos, yPos, value, matrix):
    left_visible = True
    top_visible = True
    bottom_visible = True
    right_visible = True
    # check left
    for i in range(xPos):
        if int(matrix[yPos][i]) >= value:
            left_visible = False
            break
    # check top
    for i in range(yPos):
        if int(matrix[i][xPos]) >= value:
            top_visible = False
            break
    #check bottom
    for i in range(len(matrix) - 1, yPos, -1):
        if int(matrix[i][xPos]) >= value:
            bottom_visible = False
            break
    #check right
    for i in range(len(matrix[0]) - 1, xPos, -1):
        if int(matrix[yPos][i]) >= value:
            right_visible = False
            break

    if (left_visible == False and top_visible == False and
    bottom_visible == False and right_visible == False):
        return False
    return True

def part2(lines):
    # Width and height of matrix
    height = len(lines)
    width = len(lines[0].strip())

    matrix = [[0]*height for i in range(width)]
    matrix = construct_matrix(matrix, lines)

    maximum_view = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            result = check_view_score(j, i, int(matrix[i][j]), matrix)
            if result > maximum_view:
                maximum_view = result
    print(maximum_view)

def check_view_score(xPos, yPos, value, matrix):
    # check left
    left_count = 0
    top_count = 0
    bottom_count = 0
    right_count = 0
    # left count
    for i in range(xPos, 0, -1):
        left_count += 1
        if (i-1) < 0:
            break
        if int(matrix[yPos][i-1]) >= value:
            break
    # top count
    for i in range(yPos, 0, -1):
        top_count += 1
        if (i-1) < 0:
            break
        if int(matrix[i-1][xPos]) >= value:
            break
    # bottom count
    for i in range(yPos, len(matrix) - 1):
        bottom_count += 1
        if (i+1) >= len(matrix[0]):
            break
        if int(matrix[i+1][xPos]) >= value:
            break
    # right count
    for i in range(xPos, len(matrix[0])):
        right_count += 1
        if (i+1) >= len(matrix[0]) - 1:
            break
        if int(matrix[yPos][i+1]) >= value:
            break
    return left_count * top_count * bottom_count * right_count

with open('day8.txt') as f:
    lines = f.readlines()
part1(lines)
part2(lines)