import hashlib

digests = {}

def contains_triple(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+1] == s[i+2]:
            return s[i]
    return False


def contains_5(s, c):
    return 5 * c in s


def stretch_key(salt, idx):
    if idx in digests:
        return digests[idx]
    h = hashlib.md5(salt + str(idx)).hexdigest()
    for _ in range(2016):
        h = hashlib.md5(h).hexdigest()
    digests[idx] = h
    return h


def is_key(salt, idx, part=1):
    if part == 1:
        h = hashlib.md5(salt + str(idx)).hexdigest()
    else:
        h = stretch_key(salt, idx)
    c = contains_triple(h)
    if idx % 1000 == 0:
        print idx
    if contains_triple(h):
        for i in range(1, 1001):
            if part == 1:
                h = hashlib.md5(salt + str(idx + i)).hexdigest()
            else:
                h = stretch_key(salt, idx + i)
            if contains_5(h, c):
                return True
    return False


def key_generator(salt, part):
    idx = 0
    while True:
        if is_key(salt, idx, part):
            yield idx
        idx += 1


def sixty_fourth_key(salt, part=1):
    g = key_generator(salt, part)
    for x in range(64):
        c = g.next()
    return c

if __name__ == '__main__':
    # assert not is_key('abc', 18)
    # assert is_key('abc', 39)
    # assert is_key('abc', 92)
    # assert sixty_fourth_key('abc') == 22728

    # print("Part 1: %s" % sixty_fourth_key('qzyelonm'))
    assert not is_key('abc', 5, 2)
    assert is_key('abc', 10, 2)
    assert is_key('abc', 22551, 2)

    print("Part 2: %s" % sixty_fourth_key('qzyelonm', part=2))
