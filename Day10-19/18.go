package main

import (
    "fmt"
)

const input = "^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^."

func generateRow(line []byte) (row []byte, safeTiles int) {
    newRow := make([]byte, len(line))
    safeTiles = 0

    length := len(line)

    for i := 0; i < len(line); i++ {
        if (i > 0 && line[i-1] == '^') != (i < length - 1 && line[i+1] == '^') {
            newRow[i] = '^'
        } else {
            newRow[i] = '.'
            safeTiles++
        }
    }

    return newRow, safeTiles
}

func numSafeTiles(seed string, numRows int) int {
    curr := []byte(seed)
    safeTiles := 0

    for i := 0; i < len(seed); i++ {
        if seed[i] == '.' {
            safeTiles++
        }
    }

    for i := 1; i < numRows; i++ {
        newRow, currSafe := generateRow(curr)
        safeTiles += currSafe
        curr = newRow
    }

    return safeTiles
}

func main() {
    fmt.Printf("Part 1: %d\n", numSafeTiles(input, 40))
    fmt.Printf("Part 2: %d\n", numSafeTiles(input, 400000))
}