def simulate(inst, initial_values={}):
    registers = {x: 0 for x in 'abcd'}
    registers.update(initial_values)

    def get_val(i):
        if i in registers:
            return registers[i]
        return int(i)

    instructs = map(lambda x: x.split(), inst)
    pc = 0
    pairs = {
        'inc': 'dec',
        'dec': 'inc',
        'tgl': 'inc',
        'jnz': 'cpy',
        'cpy': 'jnz',
    }
    while pc < len(instructs):
        op = instructs[pc]
        # print op
        if op[0] == 'cpy':
            if not op[2] in registers:
                print "Invalid copy: %s" % op
            registers[op[2]] = get_val(op[1])
        elif op[0] == 'inc':
            registers[op[1]] += 1
        elif op[0] == 'dec':
            registers[op[1]] -= 1
        elif op[0] == 'jnz':
            if get_val(op[1]) != 0:
                pc += get_val(op[2])
                continue
        elif op[0] == 'add':
            registers[op[1]] = get_val(op[2]) + get_val(op[3])
        elif op[0] == 'mul':
            registers[op[1]] = get_val(op[2]) * get_val(op[3])
        elif op[0] == 'tgl':
            if pc + get_val(op[1]) < len(instructs):
                c = instructs[pc + get_val(op[1])][0]
                instructs[pc + get_val(op[1])][0] = pairs[c]
        else:
            print "No opcode for %s" % op[0]
            break
        pc += 1
    return registers

if __name__ == '__main__':
    with open('23_test.txt', 'r') as f:
        assert simulate(f.readlines())['a'] == 3
    with open('23_improved.txt', 'r') as f:
        inst = f.readlines()
        print("Part 1: %s" % simulate(inst, {'a': 7})['a'])
        print("Part 2: %s" % simulate(inst, {'a': 12})['a'])