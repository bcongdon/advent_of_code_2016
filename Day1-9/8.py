import itertools


def print_display(state):
    for y in range(len(state[0])):
        row = ''.join('#' if state[i][y] else '.' for i in range(len(state)))
        print(row)
    print('\n')


def process_cmd_list(cmds):
    # pixels[x][y]
    #   inner lists are columns
    pixels = [[False for i in range(6)] for j in range(50)]
    cmds = map(lambda x: x.strip().split(), cmds)
    for cmd in cmds:
        if cmd[0] == 'rect':
            x, y = map(int, cmd[1].split('x'))
            for i, j in itertools.product(range(x), range(y)):
                pixels[i][j] = True
        if cmd[0] == 'rotate':
            rc, loc, _, amt = cmd[1:]
            loc, amt = int(loc.split('=')[-1]), int(amt)
            # column rotation
            if rc == 'column':
                pixels[loc] = pixels[loc][-amt:] + pixels[loc][:-amt]
            # row rotation
            else:
                row = [pixels[i][loc] for i in range(len(pixels))]
                row = row[-amt:] + row[:-amt]
                for i in range(len(pixels)):
                    pixels[i][loc] = row[i]
    return sum(1 for i in pixels for j in i if j), pixels


if __name__ == '__main__':
    with open('8-test.txt', 'r') as f:
        assert process_cmd_list(f.readlines())[0] == 6
    with open('8.txt', 'r') as f:
        amt, res = process_cmd_list(f.readlines())
        print("Part 1: %s" % amt)
        print("Part 2:")
        print_display(res)
