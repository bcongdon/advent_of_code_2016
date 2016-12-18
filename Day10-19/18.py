def generate_pattern(seed, rows):
    r = row_generator(seed)
    return [r.next() for _ in range(rows)]


def row_generator(seed):
    prev = [i == '^' for i in seed]
    yield prev
    while True:
        c = [(i > 0 and prev[i-1]) ^ (i+1 < len(seed) and prev[i+1])
             for i in range(len(seed))]
        prev = c
        yield c


def prettify(arr):
    return '\n'.join(''.join('^' if i else '.' for i in r) for r in arr)


def num_safe(arr):
    return sum(1 if not i else 0 for r in arr for i in r)

if __name__ == '__main__':
    assert num_safe(generate_pattern('..^^.', 3)) == 6
    assert num_safe(generate_pattern('.^^.^.^^^^', 10)) == 38

    with open('18.txt', 'r') as f:
        inp = f.read()
        print("Part 1: %s" % num_safe(generate_pattern(inp, 40)))

        p2, r = 0, row_generator(inp)
        for i in range(400000):
            p2 += sum(1 if not i else 0 for i in r.next())
        print("Part 2: %s" % p2)
