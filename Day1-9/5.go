package main

import (
    "fmt"
    "crypto/md5"
    "encoding/hex"
    "strconv"
)

type result struct {
    worked bool
    result string
}

func tryHash(prefix string, suffix int) result {
    str := fmt.Sprintf("%s%d", prefix, suffix)
    hasher := md5.New()
    hasher.Write([]byte(str))
    digest := hex.EncodeToString(hasher.Sum(nil))
    for i := 0; i < 5; i++ {
        if digest[i] != '0' {
            return result{worked: false}
        }
    }
    return result{worked: true, result: digest}
}

func part1(input string) string {
    l := 0
    out := make([]byte, 8)

    for c := 0; l < 8; c++ {
        r := tryHash(input, c)
        if r.worked {
            out[l] = r.result[5]
            l++
        }
    }
    return string(out)
}

func part2(input string) string {
    l := 0
    out := []byte{0, 0, 0, 0, 0, 0, 0, 0}

    for c := 0; l < len(out); c++ {
        r := tryHash(input, c)
        if r.worked {
            pos, err := strconv.Atoi(string(r.result[5]))
            if err == nil && pos < len(out) && out[pos] == 0 {
                out[pos] = r.result[6]
                l++
            }
        }
    }
    return string(out)
}

func main() {
    const input = "wtnhxymk"
    fmt.Printf("Part 1: %s\n", part1(input))
    fmt.Printf("Part 2: %s\n", part2(input))
}