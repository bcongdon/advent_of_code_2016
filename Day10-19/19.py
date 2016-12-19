from math import log


def elf_exchange(num):
    b = bin(num)[2:]
    return int(b[1:] + b[0], 2)


def elf_exchange_2(num):
    i = 3**int(log(num, 3))
    if num == i:
        return num
    else:
        return max(num - i, 2*num - 3*i)


if __name__ == '__main__':
    assert elf_exchange(5) == 3
    print("Part 1: %s" % elf_exchange(3005290))
    assert elf_exchange_2(5) == 2
    print("Part 2: %s" % elf_exchange_2(3005290))
