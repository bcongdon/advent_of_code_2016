package main

import (
    "fmt"
    "strings"
    "io/ioutil"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func sslFields(r rune) bool {
    return r == '[' || r == ']'
}

func containsABBA(str string) bool {
    for i := 0; i < len(str) - 3; i++ {
        if(str[i] == str[i+3] && str[i+1] == str[i+2] && str[i] != str[i+1]) {
            return true
        }
    }
    return false
}

func supportsTLS(addr string) bool {
    chunks := strings.FieldsFunc(addr, sslFields)
    supportInside := false
    for i, chunk := range chunks {
        if i % 2 == 0 {
            // Not inside brackets
            if containsABBA(chunk) {
                supportInside = true
            }
        } else {
            // Inside brackets
            if containsABBA(chunk) {
                return false
            }
        }
    }
    return supportInside
}

func extractABAS(chunk string) []string {
    found := 0
    abas := make([]string, len(chunk))
    for i := 0; i < len(chunk) - 2; i++ {
        if chunk[i] == chunk[i+2] && chunk[i] != chunk[i+1] {
            abas[found] = chunk[i:i+3]
            found++
        }
    }
    return abas[:found]
}

func supportsSSL(addr string) bool {
    chunks := strings.FieldsFunc(addr, sslFields)
    abas := make([]string, 0)
    babs := make(map[string]bool)
    for i, chunk := range chunks {
        if i % 2 == 0 {
            // Not inside brackets
            abas = append(abas, extractABAS(chunk)...)
        } else {
            // Inside brackets
            for _, bab := range extractABAS(chunk) {
                babs[bab] = true
            }
        }
    }
    for _, aba := range abas {
        corresponding := fmt.Sprintf("%c%c%c", aba[1], aba[0], aba[1])
        if _, ok := babs[corresponding]; ok {
            return true
        }
    }
    return false
}

func part1(addresses []string) int {
    c := 0
    for _, str := range addresses {
        if(supportsTLS(str)) {
            c++
        }
    }
    return c
}

func part2(addresses []string) int {
    c := 0
    for _, str := range addresses {
        if(supportsSSL(str)) {
            c++
        }
    }
    return c
}

func main() {
    dat, err := ioutil.ReadFile("./7.txt")
    check(err)
    lines := strings.Split(string(dat), "\n")
    fmt.Printf("Part 1: %d\n", part1(lines))
    fmt.Printf("Part 2: %d\n", part2(lines))
}