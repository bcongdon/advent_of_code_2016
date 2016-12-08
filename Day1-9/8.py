# -*- coding: utf-8 -*-
import itertools
import sys
from time import sleep


def print_display(state):
    sys.stdout.write('\033c')
    out = ''
    for y in range(len(state[0])):
        out += ''.join('█' if state[i][y] else ' ' for i in range(len(state)))
        out += '\n'
    print(out)


def process_cmd_list(cmds, animate=False):
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
        if animate:
            print_display(pixels)
            sleep(0.05)
    return sum(1 for i in pixels for j in i if j), pixels


if __name__ == '__main__':
    with open('8-test.txt', 'r') as f:
        assert process_cmd_list(f.readlines())[0] == 6
    with open('8.txt', 'r') as f:
        amt, res = process_cmd_list(f.readlines(), animate=True)
        print("Part 1: %s" % amt)
        print("Part 2: See above. :)")
