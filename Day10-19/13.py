from collections import defaultdict


def num_bits(n):
    c = 0
    while n > 0:
        c += 1
        n = n & (n - 1)
    return c


def is_wall(x, y, i):
    s = x*x + 3*x + 2*x*y + y + y*y + i
    return num_bits(s) % 2 == 1


def m_dist(src, dest):
    (x1, y1), (x2, y2) = src, dest
    return (x2 - x1) + (y2 - y1)


def is_valid(nbr, n):
    x, y = nbr
    return not (x < 0 or y < 0 or is_wall(x, y, n))


def path_find(tx, ty, n, part=1):
    visited, to_visit = set(), set([(1, 1)])

    step_score = defaultdict(lambda: 2**32)
    step_score[(1, 1)] = 0

    dist_map = defaultdict(lambda: 2**32)
    dist_map[(1, 1)] = m_dist((1, 1), (tx, ty))

    while to_visit:
        _, c = min(((dist_map[i], i) for i in to_visit), key=lambda x: x[0])
        if c == (tx, ty) and part == 1:
            return step_score[c]
        to_visit.remove(c)
        visited.add(c)
        if part == 2 and step_score[c] >= 50:
            continue
        cx, cy = c
        for nbr in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            if nbr in visited or not is_valid(nbr, n):
                continue
            t_score = step_score[c] + 1
            to_visit.add(nbr)
            if t_score >= step_score[nbr]:
                continue
            step_score[nbr] = t_score
            dist_map[nbr] = t_score + m_dist(nbr, (tx, ty))
    return len(step_score)

if __name__ == '__main__':
    assert path_find(7, 4, 10) == 11

    print("Part 1: %s steps to (31, 39)" % path_find(31, 39, 1364))
    print("Part 2 %s unique destinations possible" %
          path_find(31, 39, 1364, part=2))
