import re


def decompress(s):
    c, out, pat = 0, "", re.compile(r"\((\d+)x(\d+)\)")
    while c < len(s):
        m = pat.match(s[c:])
        if m:
            l, rep = map(int, m.groups())
            c += len(m.group(0))
            out, c = out + s[c:c+l] * rep, c + l
        else:
            out, c = out + s[c], c + 1
    return out


def decompress2(s):
    count, i, pat = 0, 0, re.compile(r"\((\d+)x(\d+)\)")
    while i < len(s):
        m = pat.match(s[i:])
        if m:
            l, rep = map(int, m.groups())
            i += len(m.group(0))
            count, i = count + decompress2(s[i:i+l]) * rep, i + l
        else:
            count, i = count + 1, i + 1
    return count


if __name__ == '__main__':
    pt1_tests = {
        'ADVENT': 'ADVENT',
        'A(1x5)BC': 'ABBBBBC',
        '(3x3)XYZ': 'XYZXYZXYZ',
        'A(2x2)BCD(2x2)EFG': 'ABCBCDEFEFG',
        '(6x1)(1x3)A': '(1x3)A',
        'X(8x2)(3x3)ABCY': 'X(3x3)ABC(3x3)ABCY'
    }
    assert all(map(lambda x: decompress(x[0]) == x[1], pt1_tests.iteritems()))

    pt2_tests = {
        '(3x3)XYZ': 9,
        'X(8x2)(3x3)ABCY': len('XABCABCABCABCABCABCY'),
        '(27x12)(20x12)(13x14)(7x10)(1x12)A': 241920,
        '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN': 445
    }
    assert all(map(lambda x: decompress2(x[0]) == x[1], pt2_tests.iteritems()))

    with open('9.txt', 'r') as f:
        puzzle = f.read().strip()
        print('Part 1: %s' % len(decompress(puzzle)))
        print('Part 2: %s' % decompress2(puzzle))
