from collections import Counter


def decrypt_message(lines):
    counters = map(lambda _: Counter(), range(len(lines[0])))
    [counters[i].update(c) for line in lines for i, c in enumerate(line)]
    return ''.join(map(lambda x: x.most_common(1)[0][0], counters))


def decrypt_message_p2(lines):
    counters = map(lambda _: Counter(), range(len(lines[0])))
    [counters[i].update(c) for line in lines for i, c in enumerate(line)]
    return ''.join(map(lambda x: x.most_common()[-1][0], counters))


def read_and_strip(fname):
    with open(fname, 'r') as f:
        return map(lambda x: x.strip(), f.read().split())

if __name__ == '__main__':
    assert decrypt_message(read_and_strip('6-test.txt')) == 'easter'
    assert decrypt_message_p2(read_and_strip('6-test.txt')) == 'advent'

    print('Part 1: %s' % decrypt_message(read_and_strip('6.txt')))
    print('Part 2: %s' % decrypt_message_p2(read_and_strip('6.txt')))
