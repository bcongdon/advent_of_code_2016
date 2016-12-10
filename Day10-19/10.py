from collections import defaultdict


def process_bots(cmds):
    bots, output, edges = defaultdict(list), defaultdict(list), {}
    for cmd in map(lambda x: x.split(), cmds):
        if cmd[0] == 'value':
            bots[int(cmd[-1])].append(int(cmd[1]))
        else:
            l, h = map(int, (cmd[6], cmd[-1]))
            edges[int(cmd[1])] = (l, cmd[5], h, cmd[-2])
    while bots:
        try:
            bot, inv = next((k, v) for k, v in bots.iteritems() if len(v) == 2)
        except StopIteration:
            break
        bots[bot] = []
        l, l_io, h, h_io = edges[bot]
        if 61 in inv and 17 in inv:
            print "Part 1: %s" % bot
        (bots if l_io == 'bot' else output)[l].append(min(inv))
        (bots if h_io == 'bot' else output)[h].append(max(inv))
    return {k: v[0] for k, v in output.items()}


if __name__ == '__main__':
    with open('10-test.txt', 'r') as f:
        process_bots(f.readlines())

    with open('10.txt', 'r') as f:
        o = process_bots(f.readlines())
        print("Part 2: %s" % (o[0] * o[1] * o[2]))
