package main

import (
	"fmt"
)

func main() {
	var (
		n, m, q int
		M = [1024][1024]int{}
		S = [1024][1024]string{}
	)
	fmt.Scan(&n, &m, &q)

	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Scan(&M[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Scan(&S[i][j])
		}
	}

	fmt.Println("digraph {\n\trankdir = LR\n\tdummy [label = \"\", shape = none]")
	for i := 0; i < n; i++ {
		fmt.Printf("\t%d [shape = circle]\n", i)
	}
	fmt.Printf("\tdummy -> %v\n", q)
	for i := 0; i < n; i++ {
		for j := 0; j < m; j++ {
			fmt.Printf(
				"\t%d -> %d  [label = \"%s(%s)\"]\n",
				i,
				M[i][j],
				string(rune(97+j)),
				S[i][j],
			)
		}
	}
	fmt.Print("}\n")
}
