from collections import Counter


def decrypt_message(lines):
    return ''.join(Counter(i).most_common()[0][0] for i in zip(*lines))


def decrypt_message_p2(lines):
    return ''.join(Counter(i).most_common()[-1][0] for i in zip(*lines))


def read_and_strip(fname):
    with open(fname, 'r') as f:
        return map(lambda x: x.strip(), f.read().split())

if __name__ == '__main__':
    assert decrypt_message(read_and_strip('6-test.txt')) == 'easter'
    assert decrypt_message_p2(read_and_strip('6-test.txt')) == 'advent'

    print('Part 1: %s' % decrypt_message(read_and_strip('6.txt')))
    print('Part 2: %s' % decrypt_message_p2(read_and_strip('6.txt')))
