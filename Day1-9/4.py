from collections import Counter


def is_valid_room(room):
    cs = room[-6:-1]
    e = ''.join(room.split('-')[:-1])
    c = Counter(e).most_common()
    counts = map(lambda x: x[1], c)
    counts = sorted(list(set(counts)), reverse=True)
    e_check = ''
    for count in counts:
        letters = map(lambda x: x[0], filter(lambda x: x[1] == count, c))
        letters.sort()
        e_check += ''.join(letters)
    return cs == e_check[:5]


def get_sector_id(room):
    return int(room.split('[')[0].split('-')[-1])


def decode_sector(room):
    s = get_sector_id(room)
    decoded = ''
    for c in ' '.join(room.split('-')[:-1]):
        if c != ' ':
            offset = s % 26
            if chr(ord(c) + offset) > 'z':
                offset -= 26
            c = chr(ord(c) + offset)
        decoded += c
    return decoded


if __name__ == '__main__':
    assert is_valid_room('aaaaa-bbb-z-y-x-123[abxyz]')
    assert is_valid_room('a-b-c-d-e-f-g-h-987[abcde]')
    assert is_valid_room('not-a-real-room-404[oarel]')
    assert not is_valid_room('totally-real-room-200[decoy]')

    with open('4.txt', 'r') as f:
        sector_sum = 0
        real_rooms = []
        for r in f:
            r = r.strip()
            if is_valid_room(r):
                real_rooms.append(r)
                sector_sum += get_sector_id(r)
        print('Part 1: %s' % sector_sum)

        for r in real_rooms:
            real_name = decode_sector(r)
            if 'pole' in real_name:
                print('Part 2: {} is in sector {}'.format(real_name,
                                                          get_sector_id(r)))
