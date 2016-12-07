import re

def contains_abba(a):
    if len(a) < 4:
        return False
    return any(a[i] == a[i+3] and a[i+1] == a[i+2] and
               a[i] != a[i+1]
               for i in range(len(a) - 3))


def supports_tls(line):
    pat = re.compile(r'\[|\]')
    arr = pat.split(line)
    found = False
    for idx, i in enumerate(arr):
        res = contains_abba(i)
        if idx % 2 == 0 and res:
            found = True
        elif idx % 2 == 1 and res:
            return False
    return found


if __name__ == '__main__':
    assert supports_tls('abba[mnop]qrst')
    assert not supports_tls('abcd[bddb]xyyx')
    assert not supports_tls('aaaa[qwer]tyui')
    assert supports_tls('ioxxoj[asdfgh]zxcvbn')

    with open('7.txt', 'r') as f:
        lines = f.read().split()
        s = sum(1 for i in lines if supports_tls(i))
        print('Part 1: %s' % s)
