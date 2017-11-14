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

const DELIMITER = ","

type Direction int
type Cardinal int

const (
	L Direction = 1
	R Direction = 2
)

type Move struct {
	direction Direction
	distance  int
}

type Location struct {
	x int
	y int
}

func parseDirection(str string) Direction {
	if str == "L" {
		return L
	} else if str == "R" {
		return R
	}
	return -1
}

func abs(i int) int {
	if i < 0 {
		return -i
	}
	return i
}

func parseMoves(str string) []Move {
	splitStr := strings.Split(str, DELIMITER)
	moves := make([]Move, len(splitStr))
	for i, moveStr := range strings.Split(str, DELIMITER) {
		moveStr = strings.TrimSpace(moveStr)
		dist, _ := strconv.Atoi(moveStr[1:])
		m := Move{direction: parseDirection(moveStr[:1]), distance: dist}
		moves[i] = m
	}
	return moves
}

func shortestPath(moves []Move) int {
	x, y := 0, 0
	xSign := 0
	ySign := 1
	for _, move := range moves {
		if move.direction == R {
			tmp := xSign
			xSign = ySign
			ySign = -tmp
		} else {
			tmp := ySign
			ySign = xSign
			xSign = -tmp
		}

		x += xSign * move.distance
		y += ySign * move.distance
	}
	return abs(x) + abs(y)
}

func firstRevisitedDist(moves []Move) int {
	seen := map[Location]bool{}

	x, y := 0, 0
	xSign := 0
	ySign := 1
	for _, move := range moves {
		if move.direction == R {
			tmp := xSign
			xSign = ySign
			ySign = -tmp
		} else {
			tmp := ySign
			ySign = xSign
			xSign = -tmp
		}

		for i := 0; i < move.distance; i++ {
			x += xSign
			y += ySign
			loc := Location{x: x, y: y}
			_, exists := seen[loc]
			if exists {
				return abs(x) + abs(y)
			}
			seen[loc] = true
		}
	}
	return -1
}

func main() {
	// Println outputs a line to stdout.
	// Qualify it with the package name, fmt.
	dat, err := ioutil.ReadFile("./1.txt")
	check(err)
	moves := parseMoves(string(dat))
	fmt.Printf("Part 1: %d\n", shortestPath(moves))
	fmt.Printf("Part 2: %d\n", firstRevisitedDist(moves))
}
