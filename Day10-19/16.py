def gen_data(o, n):
    while len(o) < n:
        m = ['1' if i == '0' else '0' for i in o[::-1]]
        o += '0' + ''.join(m)
    return o[:n]


def checksum(s):
    c = ''
    for i in range(0, len(s), 2):
        c += '1' if s[i] == s[i+1] else '0'
    return c if len(c) % 2 else checksum(c)

if __name__ == '__main__':
    assert checksum(gen_data('10000', 20)) == '01100'

    print("Part 1: %s " % checksum(gen_data('10111011111001111', 272)))
    print("Part 1: %s " % checksum(gen_data('10111011111001111', 35651584)))
