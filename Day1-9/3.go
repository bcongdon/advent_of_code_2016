package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

type Triangle struct {
    lengths [3]int
}

type Triangles []Triangle

func parseTriangleLine(line string) [3]int {
    var sides [3]int
    fields := strings.Fields(line)
    for j := 0; j < 3; j++ {
        sides[j], _ = strconv.Atoi(fields[j])
    }
    return sides
}

func parseInput(str string) Triangles {
    split := strings.Split(str, "\n")
    triangles := make([]Triangle, len(split))
    for i, line := range split {
        triangles[i] = Triangle{lengths: parseTriangleLine(line)}
    }
    return triangles
}

func parseVerticalInput(str string) Triangles {
    split := strings.Split(str, "\n")
    triangles := make([]Triangle, len(split))

    for i := 0; i < len(split); i += 3 {
        var chunk [3]Triangle
        var lengths [3][3]int
        for j := 0; j < 3; j ++ {
            chunk[j] = Triangle{lengths: [3]int{0, 0, 0}}
            lengths[j] = parseTriangleLine(split[i+j])
        }
        for j := 0; j < 3; j ++ {
            for k := 0; k < 3; k++ {
                chunk[j].lengths[k] = lengths[k][j]
            }            
        }
        for j := 0; j < 3; j ++ {
            triangles[i+j] = chunk[j]
        }
    }
    return triangles
}

func (t Triangle) isValid() bool {
    for i := 0; i < 3; i ++ {
        s1 := t.lengths[i]
        s2 := 0
        for j := 0; j < 3; j ++ {
            if i == j {
                continue
            }
            s2 += t.lengths[j]
        }
        if !(s1 < s2) {
            return false
        }
    }
    return true
}

func (triangles Triangles) numValid() int {
    c := 0
    for _, t := range triangles {
        if t.isValid() {
            c ++
        }
    }
    return c
}

func main() {
    dat, err := ioutil.ReadFile("./3.txt")
    check(err)
    triangles := parseInput(string(dat))
    triangles2 := parseVerticalInput(string(dat))
    fmt.Printf("Part 1: %d\n", triangles.numValid())
    fmt.Printf("Part 2: %d\n", triangles2.numValid())
}