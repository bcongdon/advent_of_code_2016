def xy_to_digit_part_1(x, y):
    if not (0 <= x <= 2 and 0 <= y <= 2):
        return None
    return y * 3 + (x + 1)

part2_layout = [[None, None, 1, None, None],
                [None, 2, 3, 4, None],
                [5, 6, 7, 8, 9],
                [None, 'A', 'B', 'C', None],
                [None, None, 'D', None, None]]


def xy_to_digit_part_2(x, y):
    if not (0 <= x <= 4 and 0 <= y <= 4):
        return None
    return part2_layout[y][x]


def part2(commands):
    code = ''
    x, y = 0, 2
    for l in commands.split():
        digit, x, y = command_str_to_digit(l, x, y, xy_to_digit_part_2)
        code += str(digit)
    return code


def part1(commands):
    code = ''
    x = y = 1
    for l in commands.split():
        digit, x, y = command_str_to_digit(l, x, y, xy_to_digit_part_1)
        code += str(digit)
    return code


def command_str_to_digit(commands, x, y, digit_converter):
    for c in commands:
        if c == 'U':
            new_x, new_y = x, y - 1
        elif c == 'D':
            new_x, new_y = x, y + 1
        elif c == 'L':
            new_x, new_y = x - 1, y
        elif c == 'R':
            new_x, new_y = x + 1, y

        if digit_converter(new_x, new_y):
            x, y = new_x, new_y
    return digit_converter(x, y), x, y

if __name__ == '__main__':
    test_str = 'ULL\nRRDDD\nLURDL\nUUUUD'
    assert part1(test_str) == '1985'
    assert part2(test_str) == '5DB3'

    with open('2.txt', 'r') as f:
        in_str = f.read()
        print("Part 1: %s" % part1(in_str))
        print("Part 2: %s" % part2(in_str))
