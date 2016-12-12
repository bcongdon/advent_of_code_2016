
def simulate(inst, initial_values={}):
    registers = {x: 0 for x in 'abcd'}
    registers.update(initial_values)

    def get_val(i):
        if i in registers:
            return registers[i]
        return int(i)

    instructs = map(lambda x: x.split(), inst)
    pc = 0
    while pc < len(instructs):
        op = instructs[pc]
        if op[0] == 'cpy':
            registers[op[2]] = get_val(op[1])

        elif op[0] == 'inc':
            registers[op[1]] += 1
        elif op[0] == 'dec':
            registers[op[1]] -= 1
        elif op[0] == 'jnz':
            if get_val(op[1]) != 0:
                pc += get_val(op[2])
                continue
        else:
            print "No opcode for %s" % op[0]
            break
        pc += 1
    return registers

if __name__ == '__main__':
    with open('12.txt', 'r') as f:
        inst = f.readlines()
        print("Part 1: %s" % simulate(inst)['a'])
        print("Part 2: %s" % simulate(inst, {'c': 1})['a'])
