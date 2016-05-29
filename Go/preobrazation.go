package main

import (
	"fmt"
)

type element struct {
	x      int
	result string
}

func main() {
	var (
		x1, x2, n int
		state     bool
		a         element
		M         = []string{}
		S         = []string{}
		MNew      = [][]element{}
	)

	fmt.Scan(&x1)
	M = make([]string, x1)
	for i := 0; i < x1; i++ {
		fmt.Scan(&M[i])
	}

	fmt.Scan(&x2)
	S = make([]string, x2)
	for i := 0; i < x2; i++ {
		fmt.Scan(&S[i])
	}

	fmt.Scan(&n)
	MNew = make([][]element, n)
	for i := 0; i < n; i++ {
		MNew[i] = make([]element, x1)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < x1; j++ {
			fmt.Scan(&MNew[i][j].x)
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < x1; j++ {
			fmt.Scan(&MNew[i][j].result)
		}
	}

	fmt.Printf("digraph {\n\trankdir = LR\n")
	matrix, matrixNew := make(map[element]int), make(map[int]element)
	iter := 0
	for i := 0; i < n; i++ {
		for j := 0; j < x1; j++ {
			_, state = matrix[MNew[i][j]]
			if !state {
				matrix[MNew[i][j]], matrixNew[iter] = iter,
					MNew[i][j]
				fmt.Printf("\t%v [label = \"(%v,%v)\"]\n",
					iter, MNew[i][j].x, MNew[i][j].result)
				iter++
			}
		}
	}
	for i := 0; i < iter; i++ {
		for j := 0; j < x1; j++ {
			a.x, a.result = MNew[matrixNew[i].x][j].x,
				MNew[matrixNew[i].x][j].result
			fmt.Printf("\t%v -> %v [label = \"%s\"]\n", i,
				matrix[a], M[j])
		}
	}
	fmt.Printf("}\n")
}
