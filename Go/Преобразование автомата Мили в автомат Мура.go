package main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

func main () {
        var k, t, n int

	input.Scanf("%d", &k)

	s := make([]string, 0, k)

	for i := 0; i < k; i++ {
		var buf string
		input.Scanf("%s", &buf)
		s = append(s, buf)
	}

	input.Scanf("%d", &t)

	outs := make([]string, t)
	for i := 0; i < t; i++ {
		input.Scanf("%s", &outs[i])
	}


	input.Scanf("%d", &n)

	delta := make([][]int, n)
	fi := make([][]string, n)

	for i := 0; i < n; i++ {
		delta[i] = make([]int, k)
		for j := 0; j < k; j++ {
			input.Scanf("%d", &delta[i][j])
		}
	}

	for i := 0; i < n; i++ {
		fi[i] = make([]string, k)
		for j := 0; j < k; j++ {
			input.Scanf("%s", &fi[i][j])
		}
	}

	fmt.Printf("digraph {\nrankdir = LR\n")

	newi := make([]int, 0, n  * k)
	newj := make([]int, 0, n * k)

	for i := 0; i < n; i++ {
		for j := 0; j < k; j++ {
			f := 0
			for z := 0; z < len(newi); z++ {
				if (delta[newi[z]][newj[z]] == delta[i][j]) && (fi[newi[z]][newj[z]] == fi[i][j]) {
					f = 1
					break
				}
			}
			if f == 0 {
				newi = append(newi, i)
				newj = append(newj, j)
			}
		}
	}

	for i := 0; i < len(newi); i++ {
		fmt.Printf("%s%d [label = \"(%d,%s)\"]\n", fi[newi[i]][newj[i]], delta[newi[i]][newj[i]], delta[newi[i]][newj[i]], fi[newi[i]][newj[i]])
		for j := 0; j < k; j++ {
			fmt.Printf("%s%d -> %s%d [label = \"%s\"]\n", fi[newi[i]][newj[i]], delta[newi[i]][newj[i]], fi[delta[newi[i]][newj[i]]][j], delta[delta[newi[i]][newj[i]]][j], s[j])
		}
	}

	fmt.Printf("}\n")
}
