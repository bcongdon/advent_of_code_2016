from collections import deque

indecies = ['pog', 'pom', 'tmg', 'tmm', 'pmg', 'pmm', 'rug', 'rum', 'cog', 'com']

# idx = generator loc
# idx + 1 = chip loc
part1 = [1, 2, 1, 1, 1, 2, 1, 1, 1, 1]
part2 = [1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1]


def valid(state):
    f, e, _ = state
    if not 1 <= e <= 4:
        return False
    if any(not 1 <= i <= 4 for i in f):
        return False

    for idx, v in enumerate(f[1::2]):
        idx = idx * 2 + 1
        if v != f[idx - 1] and any(v == i for i in f[0::2]):
            return False
    return True


def generalize(state):
    f, e, k = state
    g = [sum(1 for v in f[::2] if v == fn) for fn in range(1, 5)]
    m = [sum(1 for v in f[1::2] if v == fn) for fn in range(1, 5)]
    return ''.join(map(str, g + m)) + str(e)


def solved(state):
    f, e, _ = state
    return all(i == 4 for i in f)


def bfs(initial_state, part):
    bfs_q = deque()
    bfs_q.append(initial_state)
    seen = set()
    nodes = 1
    while bfs_q:
        state = bfs_q.popleft()
        if generalize(state) in seen or not valid(state):
            continue
        seen.add(generalize(state))

        f, e, s = state
        if solved(state):
            print "Part %s:\tSolved in %s steps." % (part, s)
            print "\tConsidered %s nodes." % nodes
            return

        for idx in range(len(f)):
            i = f[idx]
            if i != e:  # item can't be moved bc not in elevator
                continue
            f[idx] -= 1
            bfs_q.append((list(f), e - 1, s + 1))
            f[idx] += 2
            bfs_q.append((list(f), e + 1, s + 1))
            f[idx] -= 1

            nodes += 2

            for jdx in range(idx + 1, len(f)):
                j = f[jdx]
                if j != e:
                    continue
                f[jdx] -= 1
                f[idx] -= 1
                bfs_q.append((list(f), e - 1, s + 1))
                f[jdx] += 2
                f[idx] += 2
                bfs_q.append((list(f), e + 1, s + 1))
                f[jdx] -= 1
                f[idx] -= 1
                nodes += 2
    print "Unable to solve. :("


if __name__ == '__main__':
    bfs((part1, 1, 0), 1)
    bfs((part2, 1, 0), 2)
