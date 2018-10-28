// langmealy project main.go
package main

import (
        "fmt"
        "github.com/skorobogatov/input"
)

var use, tek int

func Scan(v, col, flag, deep, n int, answer, fi [][]byte, delta [][]int) {
        if deep > col * n {
		if flag == 1 {
			tek--
		}
		return
	}

	if tek == col {
		use++
		tek--
		for i := 0; i < tek; i++ {
			answer[use][i] = answer[use - 1][i]
		}
		return
	}

	if !((delta[v][0] == v) && (fi[v][0] == '-')) {
		answer[use][tek] = fi[v][0]
		if fi[v][0] != '-' {
			tek++
			Scan(delta[v][0], col, 1, deep + 1, n, answer, fi, delta)
		} else {
			Scan(delta[v][0], col, 0, deep + 1, n, answer, fi, delta)
		}

	}

	if !((delta[v][1] == v) && (fi[v][1] == '-')) {
		answer[use][tek] = fi[v][1]
		if fi[v][1] != '-' {
			tek++
			Scan(delta[v][1], col, 1, deep + 1, n, answer, fi, delta)
		} else {
			Scan(delta[v][1], col, 0, deep + 1, n, answer, fi, delta)
		}
	}

	if flag == 1 {
		tek--
	}
}

func main() {
	var n, start, length int
	input.Scanf("%d", &n)

	fi := make([][]byte, n)
	delta := make([][]int, n)
	for i := 0; i < n; i++ {
		fi[i] = make([]byte, 2)
		delta[i] = make([]int, 2)
	}

	for i := 0; i < n; i++ {
		for j := 0; j < 2; j++ {
			input.Scanf("%d", &delta[i][j])
		}
	}
	input.Scanf("\n")
	for i := 0; i < n; i++ {
		for j := 0; j < 2; j++ {
			input.Scanf("%c ", &fi[i][j])
		}
	}

	input.Scanf("%d", &start)
	input.Scanf("%d", &length)

	for i := 1; i <= length; i++ {
		answer := make([][]byte, i * n)
		for j := 0; j < i * n; j++ {
			answer[j] = make([]byte, i)
		}
		use = 0
		tek = 0
		Scan(start, i, 0, 0, n, answer, fi, delta)

		for j := 0; j < use; j++ {
			if answer[j][0] == 0 {
				continue
			}
			for k := j + 1; k < use; k++ {
				flag := 0
				for z := 0; z < i; z++ {
					if answer[j][z] != answer[k][z] {
						flag = 1
						break
					}
				}
				if flag == 0 {
					answer[k][0] = 0
				}
			}
			for k := 0; k < i; k++ {
				fmt.Printf("%c", answer[j][k])
			}
			fmt.Printf(" ")
		}

	}

	fmt.Printf("\n")
}
