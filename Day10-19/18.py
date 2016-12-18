def generate_pattern(seed, rows):
    out = [[i == '^' for i in seed]]
    while len(out) < rows:
        c = []
        for i in range(len(seed)):
            l = out[-1][i - 1] if i > 0 else False
            r = out[-1][i + 1] if i < len(seed) - 1 else False
            c.append(l ^ r)
        out.append(c)
    return out


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
        print("Part 2: %s" % num_safe(generate_pattern(inp, 400000)))
