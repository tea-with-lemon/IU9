package main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

func qsort(n int,
	less func(i, j int) bool,
	swap func(i, j int)) {
	low := 0
	high := n - 1

	partition := func(low, high int) int {
		i, j := low, low
		for j < high{
			if less(j, high){
				swap(i, j)
				i++
			}
			j++
		}
		swap(i, high)
		return i
	}

	var qsortrec func(int, int)
	qsortrec = func(low, high int){
		if low < high{
			q := partition( low, high)
			qsortrec(low, q - 1)
			qsortrec(q + 1, high)
		}
	}

	qsortrec(low, high);
}

func main () {
	var m, n int

	input.Scanf("%d", &n)
	input.Scanf("%d", &m)

	s := make([]string, 0, m)
	x := make([]int, m)
	y := make([]int, m)

	for i := 0; i < m; i++ {
		var buf string
		input.Scanf("%d %d %s", &x[i], &y[i], &buf)
		if buf == "lambda" {
			buf = "λ"
		}
		s = append(s, buf)
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

	qsort(m,
		func (i, j int) bool { return (x[i] < x[j]) || (x[i] == x[j] && y[i] < y[j]) },
		func (i, j int) { x[i], x[j] = x[j], x[i]
				y[i], y[j] = y[j], y[i]
				s[i], s[j] = s[j], s[i]
		},
		)

	i = 0
	for i < m {
		fmt.Printf("%d -> %d [label = \"%s", x[i], y[i], s[i])
		for (i + 1 < m) && (y[i] == y[i + 1]) && (x[i] == x[i + 1]) {
			i++
			fmt.Printf(", %s", s[i])
		}
		fmt.Printf("\"]\n")
		i++
	}

	fmt.Printf("}\n")
}
