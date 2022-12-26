# Signal strength of 20th, 60th, 100th, 140th, 180th, 220th
def part1(lines):
    current_cycle = 0 
    register_value = 1
    total_result = 0
    for line in lines:
        split_line = line.split(' ')
        cycle_type = split_line[0].strip()
        if len(split_line) > 1:
            x_value = int(split_line[1].strip())
        # Handle noop cycle (1 cycle)
        if cycle_type == 'noop':
            current_cycle += 1
            if current_cycle == 20 or current_cycle == 60 or current_cycle == 100 or current_cycle == 140 or current_cycle == 180 or current_cycle == 220:
                total_result += (register_value * current_cycle)

        # Handle addx cycle (2 cycle)
        if cycle_type == 'addx':
            for i in range(2):
                current_cycle += 1
                if current_cycle == 20 or current_cycle == 60 or current_cycle == 100 or current_cycle == 140 or current_cycle == 180 or current_cycle == 220:
                    total_result += (register_value * current_cycle)
            register_value += int(x_value)
    print(total_result)

# Render capital letters
def part2(lines):
    current_cycle = 0
    sprite_position = 1
    current_pixels = ''
    for line in lines:
        split_line = line.split(' ')
        cycle_type = split_line[0].strip()
        if len(split_line) > 1:
            x_value = int(split_line[1].strip())
        # Handle noop cycle (1 cycle)
        if cycle_type == 'noop':
            current_cycle += 1
            if sprite_position == current_cycle % 40 or sprite_position+1 == current_cycle % 40 or sprite_position+2 == current_cycle % 40:
                current_pixels = current_pixels + '#'
            else:
                current_pixels = current_pixels + '.'
            if current_cycle % 40 == 0:
                print(current_pixels)
                current_pixels = ''
        # Handle addx cycle (2 cycle)
        if cycle_type == 'addx':
            for i in range(2):
                current_cycle += 1
                if sprite_position == current_cycle % 40 or sprite_position+1 == current_cycle % 40 or sprite_position+2 == current_cycle % 40:
                    current_pixels = current_pixels + '#'
                else:
                    current_pixels = current_pixels + '.'
                if current_cycle % 40 == 0:
                    print(current_pixels)
                    current_pixels = ''
            sprite_position += int(x_value)
        
with open('day10.txt') as f:
    lines = f.readlines()

part1(lines)
part2(lines)