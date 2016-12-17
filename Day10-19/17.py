import hashlib
from collections import deque


def pathfind(code, part=1):
    bfs_q, solutions = deque([(0, 0, '')]), []
    dirs = [(0, -1, 'U'),
            (0, 1, 'D'),
            (-1, 0, 'L'),
            (1, 0, 'R')
            ]
    while bfs_q:
        x, y, path = bfs_q.popleft()
        if x > 3 or x < 0 or y > 3 or y < 0:
            continue
        if x == y == 3:
            if part == 1:
                return path
            else:
                solutions.append(len(path))
            continue
        h = hashlib.md5(code + path).hexdigest()[:4]
        for i in xrange(len(dirs)):
            if h[i] in 'bcdef':
                dx, dy, p = dirs[i]
                bfs_q.append((x + dx, y + dy, path + p))
    if part == 2:
        return max(solutions)

if __name__ == '__main__':
    assert not pathfind('hijkl')
    assert pathfind('ihgpwlah') == 'DDRRRD'
    assert pathfind('kglvqrro') == 'DDUDRLRRUDRD'
    assert pathfind('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

    print("Part 1: %s" % pathfind('veumntbg'))

    assert pathfind('ihgpwlah', part=2) == 370
    assert pathfind('kglvqrro', part=2) == 492
    assert pathfind('ulqzkmiv', part=2) == 830

    print("Part 2: %s" % pathfind('veumntbg', part=2))
