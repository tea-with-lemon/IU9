package main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

func main () {
	var k, n int
	const maxlen byte = 20

	input.Scanf("%d", &k)
	s := make([]string, 0, k)

	for i := 0; i < k; i++ {
		var buf string
		input.Scanf("%s", &buf)
		s = append(s, buf)
	}

	input.Scanf("%d", &n)
	delta := make([][]int, n)
	for i := 0; i < n; i++ {
		delta[i] = make([]int, k)
		for j := 0; j < k; j++ {
			input.Scanf("%d", &delta[i][j])

		}
	}

	fmt.Printf("digraph {\nrankdir = LR\ndummy [label = \"\", shape = none]\n")
	for i := 0; i < n; i++ {
		fmt.Printf("%d [shape = ", i)
		var f int
		input.Scanf("%d", &f)
		if f == 0 {
			fmt.Printf("circle]\n")
		} else {
			fmt.Printf("doublecircle]\n")
		}
	}

	var i int
	input.Scanf("%d", &i)
	fmt.Printf("dummy -> %d\n", i)

	a := make([][]int, n)
	l := make([]int, n)
	for i = 0; i < n; i++ {
		a[i] = make([]int, n + 1)
	}

	for i = 0; i < n; i++ {
		for j := 0; j < n; j++ {
			l[j] = 0
		}

		for j := 0; j < k; j++ {
			a[delta[i][j]][l[delta[i][j]]] = j
			l[delta[i][j]]++
		}

		for j := 0; j < n; j++ {
			if l[j] == 0 {
				continue
			}
			fmt.Printf("%d -> %d [label = \"", i, j)
			for z := 0; z < l[j] - 1; z++ {
				fmt.Printf("%s, ", s[a[j][z]])
			}
			fmt.Printf("%s\"]\n", s[a[j][l[j] - 1]])
		}
	}
	fmt.Printf("}\n")
}
