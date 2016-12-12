def to_mips(inst, initial_mappings={})
    register_map = 'abcd'.chars.each_with_object({}) do |e,h|
        h[e] = '$t' + (e.ord - 'a'.ord).to_s 
    end
    init = initial_mappings.map do |k, v|
        "li \t#{register_map[k]}, #{v}"
    end
    main = inst.each_with_index.map do |line, idx|
        line = line.split(' ')
        case line[0]
        when 'cpy'
            dst = register_map[line[2]]
            src = register_map.fetch(line[1], line[1].to_i)
            "l#{idx}: \tadd \t#{dst}, $0, #{src}"
        when 'inc'
            reg = register_map[line[1]]
            "l#{idx}: \tadd \t#{reg}, #{reg}, 1"
        when 'dec'
            reg = register_map[line[1]]
            "l#{idx}: \tsub \t#{reg}, #{reg}, 1"
        when 'jnz'
            reg = register_map.fetch(line[1], line[1].to_i)
            off = line[2].to_i
            "l#{idx}: \tbne \t$0, #{reg}, l#{idx + off}"
        end
    end
    text = ".text\nmain:\n"
    text += "#{init.join("\n")}\n"
    text += "#{main.join("\n")}\n"
    text += "\tmove \t$a0, #{register_map['a']}\n"
    text += "\tli \t$v0, 1\n"
    text += "\tsyscall\n"
    text
end


File.open('12.txt', 'r') do |f|
    aoc_asm = f.read.split("\n")
    File.open('12_1.s', 'w+') do |w|
        mips = to_mips(aoc_asm)
        w.write mips
        puts mips
    end
    File.open('12_2.s', 'w+') do |w|
        mips = to_mips(aoc_asm, 'c' => 1)
        w.write mips
        puts mips
    end
end