import itertools


def parse_input(inp):
    inp = map(lambda x: x.split(" "), inp)
    return [(int(l[3]), int(l[-1][:-2])) for l in inp]


def check_solution(setup, time):
    return all((setup[i][1] + time + i + 1) % setup[i][0] == 0
               for i in range(len(setup)))


def get_first_drop_time(init):
    for i in itertools.count():
        if check_solution(setup, i):
            return i


if __name__ == '__main__':
    with open('15.txt', 'r')as f:
        setup = parse_input(f.readlines())
        print("Part 1: %s" % get_first_drop_time(setup))
        setup.append((11, 0))
        print("Part 2: %s" % get_first_drop_time(setup))
