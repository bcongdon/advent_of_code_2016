def taxi_dist(x, y):
    return abs(x) + abs(y)


def part1(commands):
    x = y = 0
    curr_dir = (0, 1)
    for c in commands:
        turn, dist = c[0], c[1:]
        dist = int(dist)
        curr_dir = ((curr_dir[1], -curr_dir[0]) if turn == 'R'
                    else (-curr_dir[1], curr_dir[0]))
        x += curr_dir[0] * dist
        y += curr_dir[1] * dist
    return taxi_dist(x, y)


def part2(commands):
    visited = {}
    x = y = 0
    curr_dir = (0, 1)
    for c in commands:
        turn, dist = c[0], c[1:]
        dist = int(dist)
        curr_dir = ((curr_dir[1], -curr_dir[0]) if turn == 'R'
                    else (-curr_dir[1], curr_dir[0]))
        for _ in range(dist):
            x += curr_dir[0]
            y += curr_dir[1]
            if (x, y) in visited:
                return taxi_dist(x, y)
            visited[(x, y)] = True

if __name__ == '__main__':
    # Unit Tests
    assert part1(['R2', 'L3']) == 5
    assert part1(['R2', 'R2', 'R2']) == 2
    assert part1(['R5', 'L5', 'R5', 'R3']) == 12

    assert part2(['R8', 'R4', 'R4', 'R8']) == 4

    # Puzzles
    with open('1.txt', 'r') as f:
        commands = f.read().split(', ')

    print("Part 1: {}".format(part1(commands)))
    print("Part 2: {}".format(part2(commands)))
