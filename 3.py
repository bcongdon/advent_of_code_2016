def is_valid_triangle(sides):
    s, m = sum(sides), max(sides)
    return m < (s - m)

if __name__ == '__main__':
    with open('3.txt', 'r') as f:
        count = 0
        for line in f:
            triangle = map(int, line.split())
            count += 1 if is_valid_triangle(triangle) else 0
        print('Part 1: %s' % count)

        f.seek(0)  # Reset file
        count = 0
        lines = f.readlines()
        for x in range(0, len(lines), 3):
            a, b, c = map(lambda x: map(int, x.split()), lines[x:x+3])
            for i in xrange(3):
                t = a[i], b[i], c[i]
                count += 1 if is_valid_triangle(t) else 0
        print('Part 2: %s' % count)
