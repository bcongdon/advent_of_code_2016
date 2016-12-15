import re
import itertools

abba_pat = re.compile(r'(.)((?!\1).)\2\1')


def get_aba(a):
    return [a[i:i+3] for i in range(len(a) - 2) if
            a[i] == a[i+2] and a[i] != a[i+1]]


def supports_tls(line):
    pat, found = re.compile(r'\[|\]'), False
    for idx, i in enumerate(pat.split(line)):
        res = abba_pat.search(i)
        if idx % 2 == 0 and res:
            found = True
        elif idx % 2 == 1 and res:
            return False
    return found


def supports_ssl(line):
    pat = re.compile(r'\[|\]')
    arr = pat.split(line)
    abas = list(itertools.chain.from_iterable(map(get_aba, arr[0::2])))
    babs = map(lambda i: '{0}{1}{0}'.format(i[1], i[0]), abas)
    return any(any(x in i for x in babs) for i in arr[1::2])


if __name__ == '__main__':
    assert supports_tls('abba[mnop]qrst')
    assert not supports_tls('abcd[bddb]xyyx')
    assert not supports_tls('aaaa[qwer]tyui')
    assert supports_tls('ioxxoj[asdfgh]zxcvbn')

    assert supports_ssl('aba[bab]xyz')
    assert not supports_ssl('xyx[xyx]xyx')
    assert supports_ssl('aaa[kek]eke')
    assert supports_ssl('zazbz[bzb]cdb')

    with open('7.txt', 'r') as f:
        lines = f.read().split()
        s1 = sum(1 for i in lines if supports_tls(i))
        s2 = sum(1 for i in lines if supports_ssl(i))
        print('Part 1: %s' % s1)
        print('Part 2: %s' % s2)
