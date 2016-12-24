from itertools import combinations, permutations
from collections import deque


def parse_graph(lines):
    dests, grid = {}, [[False]*len(lines) for _ in range(len(lines[0]))]
    for y, r in enumerate(lines):
        for x, c in enumerate(r):
            if c == '.':
                grid[x][y] = True
            elif unicode(c).isnumeric():
                dests[int(c)] = (x, y)
                grid[x][y] = True
    return dests, grid


def bfs(grid, start, end):
    bfs_q = deque([start + (0,)])
    seen = set()
    while bfs_q:
        x, y, c = bfs_q.popleft()
        if ((x, y) in seen or not grid[x][y]):
            continue
        seen.add((x, y))
        if (x, y) == end:
            return c
        bfs_q.append((x+1, y, c+1))
        bfs_q.append((x-1, y, c+1))
        bfs_q.append((x, y+1, c+1))
        bfs_q.append((x, y-1, c+1))


def tsp(dests, grid):
    dists = {}
    for p1, p2 in combinations(dests.keys(), 2):
        dists[p1, p2] = bfs(grid, dests[p1], dests[p2])
        dists[p2, p1] = dists[p1, p2]
    min1, min2 = 2**31, 2**31
    path_dests = dests.keys()
    path_dests.remove(0)
    for pot_path in permutations(path_dests, len(path_dests)):
        d = dists[0, pot_path[0]] + sum(dists[pot_path[i], pot_path[i-1]]
                                        for i in range(1, len(pot_path)))
        min1, min2 = min(d, min1), min(d + dists[0, pot_path[-1]], min2)
    return min1, min2


if __name__ == '__main__':
    with open('24.txt', 'r') as f:
        dests, grid = parse_graph(f.readlines())
        p1, p2 = tsp(dests, grid)
        print("Part 1: %s" % p1)
        print("Part 2: %s" % p2)
