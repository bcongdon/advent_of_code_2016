from itertools import permutations


def parse_drives(l):
    drives = []
    for r in map(lambda x: x.split(), l[2:]):
        n = map(lambda x: int(x[1:]), r[0].split('-')[-2:])
        u, a = map(lambda x: int(x[:-1]), (r[2:4]))
        drives.append((n, u, a))
    return drives


def num_pairs(drives):
    return sum(1 for d1, d2 in permutations(drives, 2)
               if d1[1] != 0 and d1[1] <= d2[2])


def pprint_grid(drives):
    x = max(drives, key=lambda x: x[0][0])[0][0]
    y = max(drives, key=lambda x: x[0][1])[0][1]
    grid = [[' '] * (x+1) for _ in range(y+1)]
    for d in drives:
        n, u, a = d
        c = '.'
        if a < 20 and u > 100:
            c = '#'
        elif u == 0:
            c = '_'
        if n[0] == x and n[1] == 0:
            c = 'G'
        if n[0] == n[1] == 0:
            c = '*'
        grid[n[1]][n[0]] = c
    for r in grid:
        print ''.join(r)

if __name__ == '__main__':
    with open('22.txt', 'r') as f:
        drives = parse_drives(f.readlines())
        print("Part 1: %s" % num_pairs(drives))
        pprint_grid(drives)
        tot_steps = 22          # Steps left
        tot_steps += 18         # Steps up
        tot_steps += 22         # Steps right
        tot_steps += 5*(35)     # Cycle move to the left
        tot_steps += 1          # Last fixing step
        print("Part 2: %s" % tot_steps)
