import hashlib
from collections import deque


def pathfind(code, part=1):
    bfs_q = deque([(0, 0, '')])
    solutions = []
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
        if h[0] in 'bcdef':
            bfs_q.append((x, y - 1, path + 'U'))
        if h[1] in 'bcdef':
            bfs_q.append((x, y + 1, path + 'D'))
        if h[2] in 'bcdef':
            bfs_q.append((x - 1, y, path + 'L'))
        if h[3] in 'bcdef':
            bfs_q.append((x + 1, y, path + 'R'))
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
