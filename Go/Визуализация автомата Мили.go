package main

import (
        "fmt"
	"github.com/skorobogatov/input"
)

func main() {
	var n int
	input.Scanf("%d\n", &n)

	fi := make([][]byte, n)
	delta := make([][]int, n)
	for i := 0; i < n; i++ {
		fi[i] = make([]byte, 3)
		delta[i] = make([]int, 3)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			input.Scanf("%d", &delta[i][j])
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			input.Scanf("%c", &fi[i][j])
		}
	}

	fmt.Printf("digraph {\nrankdir = LR\n")
	for i := 0; i < n; i++ {
		for j := 0; j < 3; j++ {
			fmt.Printf("%d -> %d [label = \"%c(%c)\"]\n", i, delta[i][j], 'a' + j, fi[i][j])
		}
	}
	fmt.Printf("}\n")
}
