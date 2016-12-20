def valid_ips(blocklist):
    ranges = [map(int, e.strip().split('-')) for e in blocklist]
    ranges.sort(key=lambda x: x[0])
    merged = [ranges[0]]
    for i in range(len(ranges)):
        t = merged[-1]
        if t[1] < ranges[i][0]:
            merged.append(ranges[i])
        elif(t[1] < ranges[i][1]):
            t[1] = ranges[i][1]
            merged.pop()
            merged.append(t)
    num_valid, first_valid, old_h = 0, 0, -1
    for r in merged:
        l, h = r
        if not num_valid and (l - old_h - 1) > 0:
            first_valid = l
        num_valid, old_h = num_valid + l - old_h - 1, h
    return first_valid, num_valid


if __name__ == '__main__':
    with open('20.txt', 'r') as f:
        f, n = valid_ips(f.readlines())
        print("Part 1: %s" % f)
        print("Part 2: %s" % n)
