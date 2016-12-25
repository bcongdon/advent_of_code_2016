package main

import (
    "fmt"
    "strings"
    "io/ioutil"
    "strconv"
    // "github.com/cznic/mathutil"
)

type Drive struct {
    x, y, used, avail int
}

    
func check(e error) {
    if e != nil {
        panic(e)
    }
}

func parseDrives(inp string) (drives []Drive) {
    lines := strings.Split(inp, "\n")
    lines = lines[2:]
    drives = make([]Drive, len(lines))
    for i, line := range lines {
        elems := strings.Fields(line)
        coords := strings.Split(elems[0], "-")
        x, _ := strconv.Atoi(coords[1][1:])
        y, _ := strconv.Atoi(coords[2][1:])
        u, _ := strconv.Atoi(elems[2][:len(elems[2]) - 1])
        a, _ := strconv.Atoi(elems[3][:len(elems[3]) - 1])
        drives[i] = Drive{x: x, y: y, used: u, avail: a}
    }
    return
}

func num_pairs(drives []Drive) (n int) {
    n = 0
    for i, d1 := range drives {
        for _, d2 := range drives[i:] {
            if(d1.used <= d2.avail && d1.used != 0) {
                n += 1
            }
            if(d2.used <= d1.avail && d2.used != 0) {
                n += 1
            }
        }
    }
    return
}

func main() {
    puzzle, err := ioutil.ReadFile("22.txt")
    check(err)
    drives := parseDrives(string(puzzle))
    fmt.Println("Part 1:", num_pairs(drives))
    steps := 22
    steps += 18
    steps += 22
    steps += 5 * 35
    steps += 1
    fmt.Println("Part 2:", steps)
}