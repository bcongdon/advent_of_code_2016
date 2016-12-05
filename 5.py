import hashlib


def decrypt_p1(e_str):
    d_str, i = '', 0
    while len(d_str) < 8:
        dig_str = e_str + str(i)
        m = hashlib.md5()
        m.update(dig_str)
        dig = m.hexdigest()
        if dig.startswith('00000'):
            d_str += dig[5]
        i += 1
    return d_str


def decrypt_p2(e_str):
    decrypted, i = [None] * 8, 0
    num_decrypted = 0
    while num_decrypted < 8:
        dig_str = e_str + str(i)
        m = hashlib.md5()
        m.update(dig_str)
        dig = m.hexdigest()
        if dig.startswith('00000'):
            try:
                idx, new_c = int(dig[5]), dig[6]
            except ValueError:
                pass
            else:
                if idx < 8 and not decrypted[idx]:
                    decrypted[idx] = new_c
                    num_decrypted += 1
        i += 1
    return ''.join(decrypted)


if __name__ == '__main__':
    assert decrypt_p1('abc') == '18f47a30'
    assert decrypt_p2('abc') == '05ace8e3'

    print('Part 1: %s' % decrypt_p1('wtnhxymk'))
    print('Part 1: %s' % decrypt_p2('wtnhxymk'))
