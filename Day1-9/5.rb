require 'digest'

INF = 1/0.0

def part1(key)
    out = ""
    (0..INF).each do |x|
        m = Digest::MD5.new
        m.update (key + x.to_s)
        d = m.hexdigest
        out << d[5] if d.start_with? '00000'
        return out if out.length == 8
    end    
end

def part2(key)
    out = Array.new(8)
    (0..INF).each do |x|
        m = Digest::MD5.new
        m.update (key + x.to_s)
        d = m.hexdigest
        if d.start_with?('00000') && /(\D+)/.match(d[5]).nil?
            i = d[5].to_i
            out[i] = d[6] unless out[i] or not (0..7) === i
            return out.join('') unless out.any? &:nil?
        end
    end    
end

puts "Part 1: #{part1 'wtnhxymk'}"
puts "Part 2: #{part2 'wtnhxymk'}"
