package main

import (
        "fmt"
	"os"
)

var white, black int

type component struct {
	start, white, black int
}

func DFS(n int, v int, k byte, matrix []byte, color []byte) {
	color[v] = k
	if k == 1 {
		white++
	} else {
		black++
	}

	for i := 0; i < n; i++ {
		if matrix[v * n + i] == '+' {
			if color[i] == 0 {
				if k == 1 {
					DFS(n, i, 2, matrix, color)
				} else {
					DFS(n, i, 1, matrix, color)
				}
			} else if color[i] == color[v] {
				fmt.Printf("No solution\n")
				os.Exit(0)
			}
		}
	}
}

func RePaint(n int, v int, k byte, matrix []byte, color []byte) {
	color[v] = k

	for i := 0; i < n; i++ {
		if matrix[v * n + i] == '+' {
			if color[i] < 3 {
				if k == 3 {
					RePaint(n, i, 4, matrix, color)
				} else {
					RePaint(n, i, 3, matrix, color)
				}
			}
		}
	}
}

func abs(a int)(int) {
	if a < 0 {
		return -a
	}
	return a
}

func main() {
	var n int

	fmt.Scanf("%d\n", &n)
	a := make([]byte, n*n)
	color := make([]byte, n)
	components := make([]component, n)

	for i := 0; i < n; i++ {
		color[i] = 0
		for j := 0; j < n; j++ {
			fmt.Scanf("%c", &a[i * n + j])
		}
		fmt.Scanf("\n")
	}
/*
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			fmt.Printf("%c ", a[i][j])
		}
		fmt.Printf("\n")

	}
*/
	comp := 0
	for i := 0; i < n; i++ {
		if color[i] == 0 {
			white, black = 0, 0
			DFS(n, i, 1, a, color)
			components[comp].start = i
			components[comp].white = white
			components[comp].black = black
			comp++
			//fmt.Printf("comp#%d: white=%d black=%d\n", comp, white, black)
		}
	}

	min := 0
	ind := make(chan int, 1 << (uint)(comp))
	for i := 0; i < comp; i++ {
		min += components[i].white - components[i].black
	}
	ind <- 0
	//fmt.Printf("%d\n", 1 << (uint)(comp))

	for i := 1; i < (1 << (uint)(comp)); i++ {
		tek := 0

		for j := 0; j < comp; j++ {
			if i & (1 << (uint)(j)) == (1 << (uint)(j)) {
				tek += components[j].black - components[j].white
			} else {
				tek += components[j].white - components[j].black
			}
		}

		//fmt.Printf("i:%d tek=%d\n", i, tek )

		if (abs(tek) < abs(min)) || (min > 0) {
			min = tek
			for len(ind) > 0 {
				<-ind
			}
			ind <- i
		} else if (tek == min) {
			ind <- i
		}
	}

	restab := make([][]byte, len(ind))
	l := len(ind)
	for i := 0; len(ind) > 0; i++ {
		restab[i] = make([]byte, n)
		for j := 0; j < n; j++ {
			restab[i][j] = color[j]
		}
		tek := <-ind
		for j := 0; j < comp; j++ {
			if tek & (1 << (uint)(j)) == (1 << (uint)(j)) {
				RePaint(n, components[j].start, 4, a, restab[i]) // 2,4 - component #2  1,3 - component #1
			}
		}
	}

	min = 2147483647
	pos := 0
	for i := 0; i < l; i++ {
		tek := 0
		for j := 0; j < n; j++ {
			if (restab[i][j] == 1) || (restab[i][j] == 3) {
				tek = tek * 10 + j + 1
			}
		}
		if tek < min {
			min, pos = tek, i
		}
		//fmt.Printf("%d\n", tek)
	}

	for i := 0; i < n; i++ {
		if (restab[pos][i] == 1) || (restab[pos][i] == 3) {
			fmt.Printf("%d ", i + 1)
		}
	}
	fmt.Printf("\n")
}
