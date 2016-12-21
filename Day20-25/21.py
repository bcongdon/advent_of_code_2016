from itertools import permutations

def scramble(inp, cmds):
    chars = list(inp)
    for c in map(lambda x: x.strip().split(' '), cmds):
        if c[0] == 'swap':
            x, y = c[2], c[5]
            if c[1] == 'position':
                x, y = map(int, (x, y))
            elif c[1] == 'letter':
                x, y = chars.index(x), chars.index(y)
            chars[x], chars[y] = chars[y], chars[x]
        elif c[0] == 'rotate':
            steps, rot = 0, 0
            if c[1] == 'left':
                steps = int(c[2]) % len(chars)
                rot = 1
            elif c[1] == 'right':
                steps = int(c[2]) % len(chars)
                rot = -1
            elif c[1] == 'based':
                idx = chars.index(c[-1])
                if idx >= 4:
                    idx += 1
                steps = idx + 1
                rot = -1
            chars = [chars[(i + rot*steps) % len(chars)]
                     for i in range(len(chars))]
        elif c[0] == 'reverse':
            x, y = map(int, (c[2], c[4]))
            chars[x:y+1] = chars[x:y+1][::-1]
        elif c[0] == 'move':
            x, y = map(int, (c[2], c[5]))
            ch = chars.pop(x)
            chars.insert(y, ch)
    return ''.join(chars)

if __name__ == '__main__':
    with open('21_test.txt', 'r') as f:
        assert scramble('abcde', f.readlines()) == 'decab'
    with open('21.txt', 'r') as f:
        cmds = f.readlines()
        print("Part 1: %s" % scramble('abcdefgh', cmds))
    unscrambled = next(p for p in permutations('abcdefgh')
                       if scramble(p, cmds) == 'fbgdceah')
    print("Part 2: %s " % ''.join(unscrambled))
